import sqlite3
import sys
from ..scriptDb.conn import Conect
from ..utils.logs import Logs

class Insert:

    def __init__(self, values, emails):

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        self.emails = emails

        self.insert = self.inserting(values)

    def inserting(self, values):

        if len(values) > 0:
            logEmail = Logs('Inserting_table_Emails')

            for i in range(len(values)):

                self.insertingRow(value=values[i], log=logEmail)
            
            logStatus = Logs('Inserting_table_status')

            for i in range(len(self.emails)):

                self.insertingRowStatus(email=self.emails[i], log=logStatus)


        self.cursor.close()
        self.conn.close()
    
    def insertingRow(self, value, log):

        try:

            self.cursor.execute(''' INSERT INTO Emails 
                        (idRow, blt, dateEmission, notes, reasonSocial, cnpj, description, valueB, valueL, dateVenc, email)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                        (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10])
                        )
            
            self.conn.commit()

            log.logger.info('Insercao de valores realizadas com sucesso na tabela Email, Id interno: {} e email: {}'. format(value[0], value[10]))
        
        except Exception as error:
            
            if isinstance(error, sqlite3.IntegrityError) and "UNIQUE constraint failed" in str(error):

                log.logger.warning('Valores ja existem na tabela Email, id Interno: {} e email: {}'.format(value[0], value[10]))

            else:
                print('ERRO - Algum erro desconhecido ocorreu durante a inseção do email: {}, Idinterno: {} no banco de dados Emails, erro: {}'.format(value[10], value[0], error))
                log.logger.error('Erro ao inserir valores na tabela Email, Id interno: {}, email: {}, erro: {}, o programa será encerrado!'. format(value[0], value[10], error))

                sys.exit()

    def insertingRowStatus(self, email, log):

        try:
            
            self.cursor.execute(''' INSERT INTO Status
                                (email, statusNote, statusBoleto, statusSend, sended) 
                                VALUES (?, ?, ?, ?, ?) ''', 
                                (email, "False", "False", 0, "False"))
            
            self.conn.commit()

            log.logger.info('Insercao de valores realizadas com sucesso na tabela Status, email: {}'.format(email))
            
        except Exception as error:

            if isinstance(error, sqlite3.IntegrityError) and "UNIQUE constraint failed" in str(error):

                log.logger.warning('Valores ja existem na tabela Status, email: {}'.format(email))

            else:

                print('ERRO - Algum erro desconhecido ocorreu durante a inseção do email: {}, no banco de dados Status, erro: {}, o programa será encerrado!'.format(email, error))
                log.logger.error('Erro ao inserir dados na tabela Status, email: {}, erro: {}'.format(email, error))

                sys.exit()