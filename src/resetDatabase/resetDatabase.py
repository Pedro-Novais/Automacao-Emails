import sys
from datetime import date
from ..utils.logs import Logs
from ..scriptDb.conn import Conect

class ResetDatabase:

    def __init__(self):

        date_today = date.today()

        self.date = date_today.strftime('%Y-%m-%d')
    
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

                self.cursor.execute('''UPDATE NumbersExecutes SET complete = ? WHERE day = ? ''', ("True", self.date))

                self.conn.commit()

                input('Os emails foram enviados com sucesso, pressione qualquer tecla para fechar a aplicação..')
                log.logger.info('Dados deletados com sucesso do banco!')

        except Exception as error:

            print('ERRO - Reset_Database - Algum erro desconhecido ocorreu ao realizar o reset do banco de dados, erro: {}'.format(error))
            log.logger.error('Algum erro desconhecido ocorreu ao realizar o reset do banco de dados, erro: {}'.format(error))

            sys.exit()