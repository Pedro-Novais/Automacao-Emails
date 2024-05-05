import json
import os
import sys
from dotenv import load_dotenv
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from ..utils.messageBaseEmail import get_message_base_html, get_line_html
from ..scriptDb.conn import Conect
from .conectServer import ConectServer
from ..utils.logs import Logs

class ConstructorMessage:

    def __init__(self, email):
        
        load_dotenv()

        self.email = email

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        self.constructor_message()

    def constructor_message(self):

        log = Logs('Constructor_Message')

        self.msg = MIMEMultipart('altenartive')

        self.msg['From'] = os.getenv('EMAIL')
        self.msg['To'] = self.email
        self.msg['Subject'] = "Financeiro E-deploy"

        self.builder_message_email(log=log)
        self.select_files_pdf(log=log)
        self.sendEmail()

    def builder_message_email(self, log):

        try:

            self.cursor.execute('SELECT * FROM Emails WHERE email = ?', (self.email,))

            datas = self.cursor.fetchall()

            self.line = ''

            for i in range(len(datas)):

                self.transform_data_from_base(datas[i])

                line = get_line_html(
                    id_interno = self.id_interno,                 
                    number_blt = self.number_boleto, 
                    date_emission = self.date_emission_formated, 
                    note_fiscal = self.fiscal_note, 
                    reason_social =  self.reason_social, 
                    cnpj = self.cnpj, 
                    description_service = self.description_service, 
                    value_bruto = self.value_brute, 
                    value_liquid = self.value_liquid, 
                    date_vencimento = self.date_venciment_formated
                    )
                
                self.line = self.line + line

            self.msg_complete = get_message_base_html(self.line)

            msg_complete = MIMEText(self.msg_complete, 'html')

            self.msg.attach(msg_complete)

            log.logger.info('Mensagem do email {} criada com sucesso'.format(self.email))
        
        except Exception as error:

            print('ERRO - Algum erro ocorreu ao criar a mensagem do email {}, erro: {}, o programa será encerrado'.format(self.email, error))
            log.logger.error('Algum erro ocorreu ao criar a mensagem do email {}, erro: {}'.format(self.email, error))

            sys.exit()

    def transform_data_from_base(self, datas):

        self.id_interno = datas[0]

        self.number_boleto = datas[1]

        date_emission = datetime.strptime(datas[2], '%Y-%m-%d %H:%M:%S')
        self.date_emission_formated = date_emission.strftime('%d/%m/%y')

        self.fiscal_note = datas[3]

        self.reason_social = datas[4]

        self.cnpj = datas[5]
        
        self.description_service = datas[6]

        value_brute = str(datas[7])
        value_brute_formated = self.verify_inexisting_zero(value_brute)
        self.value_brute = value_brute_formated.replace('.', ',')
        
        value_liquid = str(datas[8])
        value_liquid_formated = self.verify_inexisting_zero(value_liquid)
        self.value_liquid = value_liquid_formated.replace('.', ',')

        date_venciment = datetime.strptime(datas[9], '%Y-%m-%d %H:%M:%S')
        self.date_venciment_formated = date_venciment.strftime('%d/%m/%y')

    @staticmethod
    def verify_inexisting_zero(value):

        index = -1
        value_formated = value

        for i, caracter in enumerate(value):

            if caracter == '.':

                index = i

        number_after_point = index + 3

        if number_after_point != len(value):

            value_formated = '{}{}'.format(value, '0')
        
        return 'R${}'.format(value_formated)
    
    def select_files_pdf(self, log):

        try:

            self.cursor.execute(''' SELECT nameNote, nameBoleto FROM Status WHERE email = ?''', (self.email,))

            files = self.cursor.fetchall()

            files_note = json.loads(files[0][0])
            files_boleto = json.loads(files[0][1])

            self.fixed_files_pdf(
                files_note=files_note, 
                files_boleto=files_boleto,
                log=log
                )
            
            log.logger.info('Notas {} e Boletos {} selecionados com sucesso do banco de dados, Status, email: {}'.format(files_note, files_boleto, self.email))

        except Exception as error:

            print('ERRO - Algum erro inesperado ocorreu ao selecioanar as notas e boletos do email {}, erro: {}, o programa será encerrado!'.format(self.email, error))
            log.logger.info('Algum erro inesperado ocorreu ao selecioanar as notas {} e boletos {} do banco de dados do email {}, erro: {}'.format(files_note, files_boleto, self.email, error))
            sys.exit()

    def fixed_files_pdf(self, files_note, files_boleto, log):

        try:

            for i in range(len(files_note)):

                dir_note = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'pdf', 'Notas', '{}'.format(files_note[i]['nameNote'])))

                with open(dir_note, 'rb') as file:
                    
                    pdf = MIMEApplication(file.read())
                    pdf.add_header('Content-Disposition', 'attachment', filename = files_note[i]['nameNote'])
                    self.msg.attach(pdf)
            
            log.logger.info('Notas: {} do email: {}, fixadas com sucesso na mensagem a ser enviada!'.format(files_note, self.email))

            for i in range(len(files_boleto)):

                dir_note = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'pdf', 'Boletos', '{}'.format(files_boleto[i]['nameBoleto'])))

                with open(dir_note, 'rb') as file:
                    
                    pdf = MIMEApplication(file.read())
                    pdf.add_header('Content-Disposition', 'attachment', filename = files_boleto[i]['nameBoleto'])
                    self.msg.attach(pdf)

            log.logger.info('Boletos: {} do email: {}, fixadas com sucesso na mensagem a ser enviada!'.format(files_boleto, self.email))
        
        except Exception as error:

            print('Algum erro desconhcido ocorreu ao fixar os arquivos pdf na mensagem do email: {}, erro: {}, o programa será encerrado'.format(self.email, error))
            log.logger.error('Algum erro desconhcido ocorreu ao fixar os arquivos pdf na mensagem do email: {}, erro: {}'.format(self.email, error))
            sys.exit()

    def sendEmail(self):

        ConectServer(self.email, self.msg)