import sqlite3
import os
import sys
from ..utils.logs import Logs

class Conect:

    def __init__(self):

        self.conn = self.make_connection()

    def make_connection(self):

        log = Logs('Conection')

        try:  

            dir_script = os.path.dirname(os.path.abspath(__file__))

            dir_database = os.path.join(dir_script, '..', '..', 'database', 'data.db')

            conect = sqlite3.connect(dir_database)

            log.logger.info('Conexao com banco de dados realizada com sucesso')

            return conect

        except Exception as error:

            log.logger.error('Erro ao conectar com o banco de dados, erro: {}'.format(error))
            sys.exit()