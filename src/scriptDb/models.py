import sys
from .conn import Conect
from ..utils.logs import Logs

class CreateTable:

    def __init__(self):

        self.createTable()
    
    def createTable(self):

        log = Logs('Database')

        try:
            db = Conect()

            cursor = db.conn

            cursor.execute('''CREATE TABLE IF NOT EXISTS Emails (
                            idRow TEXT NOT NULL PRIMARY KEY,
                            blt TEXT NOT NULL UNIQUE,
                            dateEmission TEXT NOT NULL,
                            notes TEXT NOT NULL UNIQUE,
                            reasonSocial TEXT NOT NULL,
                            cnpj TEXT NOT NULL,
                            description TEXT NOT NULL,
                            valueB INTEGER,
                            valueL INTEGER,
                            dateVenc TEXT NOT NULL,
                            email TEXT NOT NULL
                        )''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS Status (
                            id INTEGER PRIMARY KEY,
                            email TEXT NOT NULL UNIQUE,
                            statusNote TEXT NOT NULL,
                            nameNote TEXT,
                            statusBoleto TEXT NOT NULL,
                            nameBoleto TEXT,
                            statusSend INTEGER NOT NULL,
                            sended TEXT NOT NULL    
                        ) ''')
            
            log.logger.info('Banco de dados e tabelas criadas com sucesso')
            cursor.close()
            
        except Exception as error:

            print('Erro ao criar banco de dados / tabelas: {}'.format(error))
            log.logger.error('Erro ao criar banco de dados / tabelas: {}'.format(error))
            sys.exit()