import smtplib
import ssl
import os
import time
import sys
from ..utils.logs import Logs
from smtplib import SMTPAuthenticationError
from ..scriptDb.conn import Conect
from dotenv import load_dotenv

class ConectServer:

    def __init__(self, destinatary, msg):

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        try:

            log = Logs('Conect_Server')
            
            load_dotenv()

            smtp_server = 'smtp.office365.com'
            smtp_port = 587 
            smtp_username = os.getenv('EMAIL')
            smtp_password = os.getenv('PASSWORD')

            context = ssl.create_default_context()

            with smtplib.SMTP(smtp_server, smtp_port) as server:

                server.starttls(context=context)  
                server.login(smtp_username, smtp_password) 

                log.logger.info('Login realizado com sucesso no servidor smtp')

                server.sendmail(os.getenv('EMAIL'), destinatary, msg.as_string())

                print('Email enviado com sucesso para {}'.format(destinatary))
                log.logger.info('Email enviado com sucesso para {}'.format(destinatary))
            
            self.cursor.execute(''' UPDATE Status SET sended = ? WHERE email = ?''', ("True", destinatary))

            self.conn.commit()
            log.logger.info('Email {} teve seu status atualizado para True na coluna sended, no banco de dados Status'.format(destinatary))

            time.sleep(10)

        except SMTPAuthenticationError as error:

            print('Credenciais para realizar login está incorreta, verifique o arquivo .env e tente novamente, o programa será encerrado!')
            log.logger.error('Erro ao realizar login no servidor smtp, credenciais inválidas, erro: {}'.format(error))

            sys.exit()
        
        except Exception as error:

            print('ERRO - Algum erro inesperado ocorreu ao enviar o email:{} , erro: {}, o programa será encerrado!'.format(destinatary, error))
            log.logger.error('Algum erro inesperado ocorreu ao enviar o email:{} , erro: {}'.format(destinatary, error))

            sys.exit()