import logging
import os
import sqlite3
from ..scriptDb.conn import Conect

class Insert:

    def __init__(self, values, emails):

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        self.logs()

        self.emails = emails

        # self.conn = cursor
        # self.cursor = cursor.cursor()
        self.insert = self.inserting(values)

    def inserting(self, values):

        if len(values) > 0:

            for i in range(len(values)):

                self.insertingRow(value=values[i])
            
            for i in range(len(self.emails)):

                self.insertingRowStatus(self.emails[i])


        self.cursor.close()
        self.conn.close()
    
    def insertingRow(self, value):

        try:

            self.cursor.execute(''' INSERT INTO Emails 
                        (idRow, blt, dateEmission, notes, reasonSocial, cnpj, description, valueB, valueL, dateVenc, email)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                        (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10])
                        )
            
            self.conn.commit()

            self.logger.info('Insercao de valores realizadas com sucesso, Id interno: {} e email: {}'. format(value[0], value[10]))

            #self.cursor
        
        except Exception as error:
            
            if isinstance(error, sqlite3.IntegrityError) and "UNIQUE constraint failed" in str(error):

                self.logger.warning('Valores ja existem na tabela, id Interno: {} e email: {}'.format(value[0], value[10]))

            else:
                self.logger.error('Erro ao inserir valores de Id interno: {} e email: {}, erro: {}'. format(value[0], value[10], error))

    def insertingRowStatus(self, email):
        try:
            
            self.cursor.execute(''' INSERT INTO Status
                                (email, statusNote, statusBoleto, statusSend, sended) 
                                VALUES (?, ?, ?, ?, ?) ''', 
                                (email, "False", "False", 0, "False"))
            
            self.conn.commit()

            self.logger.info('Insercao de valores realizadas com sucesso na tabela Status, email: {}'.format(email))
            
        except Exception as error:

            if isinstance(error, sqlite3.IntegrityError) and "UNIQUE constraint failed" in str(error):

                self.logger.warning('Valores ja existem na tabela Status, email: {}'.format(email))

            else:
                self.logger.error('Erro ao inserir dados na tabela Status, email: {}, erro: {}'.format(email, error))
    
    def logs(self):

        dir_script = os.path.dirname(os.path.abspath(__file__))
        dir_log = os.path.abspath(os.path.join(dir_script, '..', '..', 'logs'))

        self.logger = logging.getLogger('insertValue')
        self.logger.setLevel(logging.INFO)

        self.handler = logging.FileHandler('{}/insertValue.log'.format(dir_log))

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)