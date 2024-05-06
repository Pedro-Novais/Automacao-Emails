import sys
from ..utils.logs import Logs
from ..scriptDb.conn import Conect

class ResetDatabase:

    def __init__(self):

        log = Logs('Reset_Database')

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        try:

            self.cursor.execute('SELECT * FROM Status WHERE sended = ?', ("False",))

            email_not_send = self.cursor.fetchall()

            if len(email_not_send) == 0:

                self.cursor.execute('DELETE FROM Status WHERE sended = ?', ("True",))
                self.cursor.execute('DELETE FROM Emails')

                self.conn.commit()

                log.logger.info('Dados deletados com sucesso do banco!')

        except Exception as error:

            print('ERRO - Reset_Database - Algum erro desconhecido ocorreu ao realizar o reset do banco de dados, erro: {}'.format(error))
            log.logger.error('Algum erro desconhecido ocorreu ao realizar o reset do banco de dados, erro: {}'.format(error))

            sys.exit()