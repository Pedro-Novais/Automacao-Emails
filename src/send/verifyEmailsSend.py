import sys
from ..scriptDb.conn import Conect
from ..utils.logs import Logs
from ..utils.spaceLine import space_line

class VerifyEmailSend:

    def __init__(self):

        log = Logs('Verify_emails_already_send')

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        self.cursor.execute(''' SELECT * FROM Status WHERE statusSend = ?''', (0,))

        not_files = self.cursor.fetchall()

        # if len(not_files) > 0:

        #     space_line(100)
        #     print('WARNING - Há arquivos pdf que não foram encontrados, verifique e tente realizar o envio novamente')
        #     log.logger.warning('Há arquivos pdf que não foram encontrados, verifique e tente realizar o envio novamente')
        #     sys.exit()
        
        self.cursor.execute(''' SELECT email FROM Status WHERE sended = ?''', ("False",))

        self.emails = self.cursor.fetchall()