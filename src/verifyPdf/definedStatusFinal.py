import sys
from ..scriptDb.conn import Conect
from ..utils.logs import Logs
from ..utils.spaceLine import space_line

class DefinedStatus:

    def __init__(self):

        log = Logs('Defined_status')

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()
        
        self.get_status_files_and_set_status(log)

        self.verify_files_false(log)

    def get_status_files_and_set_status(self, log):

        try:
            self.cursor.execute(''' UPDATE Status SET statusSend = ? WHERE statusBoleto = ? AND statusNote = ?''', (1, 'True', 'True'))
            self.cursor.execute(''' UPDATE Status SET statusSend = ? WHERE statusBoleto = ? OR statusNote = ?''', (0, 'False', 'False'))

            self.conn.commit()

            log.logger.info('Status dos emails atualizado com sucesso')

        except Exception as error:

            space_line(100)
            print('ERRO - Ocorreu algum erro ao definir os status dos emails, erro: {}'.format(error))
            log.logger.error('Ocorreu algum erro ao definir os status dos emails, erro: {}'.format(error))

            sys.exit()

    def verify_files_false(self, log):

        try:

            self.cursor.execute(''' SELECT * FROM Status WHERE statusBoleto = ? OR statusNote = ?''', ("False", "False"))

            not_files = self.cursor.fetchall()

            if len(not_files) > 0:

                space_line(100)
                print('WARNING - Há arquivos pdf que não foram encontrados, verifique e tente realizar o envio novamente')
                log.logger.warning('Há arquivos pdf que não foram encontrados, verifique e tente realizar o envio novamente')
                sys.exit()

        except Exception as error:

            space_line(100)
            print('ERRO - Ocorreu um erro inesperado ao verificar os status dos emails, erro: {}'.format(error))
            log.logger.error('ERRO - Ocorreu um erro inesperado ao verificar os status dos emails, erro: {}'.format(error))
            sys.exit()