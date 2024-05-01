import sqlite3
import os

class Conect:

    def __init__(self):

        self.conn = self.connection()

    def connection(self):

        try:  

            dir_script = os.path.dirname(os.path.abspath(__file__))

            dir_database = os.path.join(dir_script, 'data.db')

            conect = sqlite3.connect(dir_database)

            print('conexão realizada com sucesso')

            return conect

        except Exception as error:

            print('Erro ao conectar com o banco de dados')
            print(error)