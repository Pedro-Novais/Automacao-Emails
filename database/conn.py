import logging
import sqlite3
import os

class Conect:

    def __init__(self):

        self.logs()

        self.conn = self.connection()

    def connection(self):

        try:  

            dir_script = os.path.dirname(os.path.abspath(__file__))

            dir_database = os.path.join(dir_script, 'data.db')

            conect = sqlite3.connect(dir_database)

            self.logger.info('Conexao com banco de dados realizada com sucesso')
            
            return conect

        except Exception as error:

            self.logger.error('Erro ao conectar com o banco de dados, erro: {}'.format(error))

            return False
        
    def logs(self):

        self.dir_script = os.path.dirname(os.path.abspath(__file__))

        self.logger = logging.getLogger('table')
        self.logger.setLevel(logging.INFO)

        self.handler = logging.FileHandler('{}/table.log'.format(self.dir_script))

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)