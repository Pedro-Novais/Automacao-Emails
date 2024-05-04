import json
import sys
from ..utils.getFiles import getFiles
from ..scriptDb.conn import Conect
from ..utils.logs import Logs
from ..utils.spaceLine import space_line

class VerifyBlt:

    def __init__(self, emails):

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        self.blt_file = getFiles('Boletos')

        self.verify(emails)

    def verify(self, emails):

        log = Logs('Verify_blt')

        for i in range(len(emails)):
        
            self.get_blt_save(emails[i], log)
                
            self.verify_blt_Files(emails[i], log)
    
    def get_blt_save(self, email, log):

        try:
            
            self.cursor.execute(''' SELECT idRow FROM Emails WHERE email = ?''', (email,))

            self.blt = self.cursor.fetchall()
        
        except Exception as error:

            print('Algum erro inesperado ocorreu ao selecionar os boletos salvos na tabela Email, email: {}, erro: {}'.format(email,error))
            log.logger.error('Algum erro inesperado ocorreu ao selecionar o boleto salvo na tabela Email, email: {}, erro: {}'.format(email, error))
            sys.exit()

    def verify_blt_Files(self, email, log):

        infos_blt = []
        self.verifyStatus = "True"

        for i in range(len(self.blt)):

            try:

                blt = self.blt[i][0]

                blt_in_files = self.compare_blt_files_and_saves(blt=blt, log=log)

                data_info_blt = {
                        "nameBoleto": blt_in_files[0],
                        "exist": blt_in_files[1]
                        }
                
                infos_blt.append(data_info_blt)

                if blt_in_files[1] == "True":

                    log.logger.info('Boleto: {}.pdf do email: {} existe!'.format(blt_in_files[0], email))

                else: 
                    
                    space_line(100)
                    print('ERRO - Boleto: {}.pdf do email: {} nao existe!'.format(blt_in_files[0], email))
                    log.logger.error('Boleto: {}.pdf do email: {} nao existe!'.format(blt_in_files[0], email))

            except Exception as error:

                self.verifyStatus = "False"
                print('Algum erro desconhecido ocorreu: {}'.format(error))
                log.logger.error('Algum erro desconhecido ocorreu: {}'.format(error))

                sys.exit()
        
        if len(infos_blt) > 0:

            dataStr = json.dumps(infos_blt)

            self.cursor.execute(''' UPDATE Status SET nameBoleto = ? WHERE email = ?''', (dataStr, email))
            self.cursor.execute(''' UPDATE Status SET statusBoleto = ? WHERE email = ?''', (self.verifyStatus, email))

            self.conn.commit()

    def compare_blt_files_and_saves(self, blt, log):

        try:

            for i in range(len(self.blt_file)):

                blt_file = self.blt_file[i]

                just_number_blt = '{}{}{}{}{}{}'.format(
                    blt_file[18],
                    blt_file[19],
                    blt_file[20],
                    blt_file[21],
                    blt_file[22],
                    blt_file[23]
                )

                if just_number_blt == blt:

                    return (blt_file, "True")
            
            self.verifyStatus = "False"

            return (blt, "False")
        
        except Exception as error:

            print(error)