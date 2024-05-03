import logging
import os
from .conn import Conect

class CreateTable:

    def __init__(self):
        
        self.logs()
    
    def createTable(self):

        try:
            db = Conect()

            cursor = db.connection()

            cursor.execute('''CREATE TABLE IF NOT EXISTS Emails (
                            idRow TEXT NOT NULL PRIMARY KEY,
                            blt TEXT NOT NULL UNIQUE,
                            dateEmission TEXT NOT NULL,
                            notes TEXT NOT NULL UNIQUE,
                            reasonSocial TEXT NOT NULL,
                            cnpj TEXT NOT NULL,
                            description TEXT NOT NULL,
                            valueB TEXT NOT NULL,
                            valueL TEXT NOT NULL,
                            dateVenc TEXT NOT NULL,
                            email TEXT NOT NULL
                        )''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Status (
                            id INTEGER PRIMARY KEY,
                            email TEXT NOT NULL UNIQUE,
                            statusNote TEXT NOT NULL,
                            nameNote TEXT,
                            statusBoleto TEXT NOT NULL,
                            nameBlt TEXT,
                            sended TEXT NOT NULL    
                        ) ''')
            
            self.logger.info('Banco de dados e tabelas criadas com sucesso')

            cursor.close()
            return True
            
        except Exception as error:

            self.logger.error('Erro ao criar banco de dados / tabelas: {}'.format(error))

    def logs(self):

        self.dir_script = os.path.dirname(os.path.abspath(__file__))

        self.logger = logging.getLogger('table')
        self.logger.setLevel(logging.INFO)

        self.handler = logging.FileHandler('{}/table.log'.format(self.dir_script))

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)