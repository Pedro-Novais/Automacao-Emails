import json
import sys
from ..utils.getFiles import getFiles
from ..scriptDb.conn import Conect
from ..utils.logs import Logs
from ..utils.spaceLine import space_line

class VerifyNotes:

    def __init__(self, emails):

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        self.notes_file = getFiles('Notas')

        self.verify(emails)

    def verify(self, emails):

        log = Logs('Verify_Notes')

        for i in range(len(emails)):
            
            self.getNoteSave(emails[i], log)
                
            self.verifyNotesFiles(emails[i], log)

    def getNoteSave(self, email, log):

        try:
            
            self.cursor.execute(''' SELECT notes FROM Emails WHERE email = ?''', (email,))

            self.notes = self.cursor.fetchall()
        
        except Exception as error:

            print('Algum erro inesperado ocorreu ao selecionar as notas salvas na tabela Email, erro: {}, o programa será encerrado!'.format(error))
            log.logger.error('Algum erro inesperado ocorreu ao selecionar as notas salvas na tabela Email, erro: {}'.format(error))

            sys.exit()

    def verifyNotesFiles(self, email, log):

        infos_note = []
        self.verifyStatus = "True"

        for i in range(len(self.notes)):

            try:

                note = self.notes[i][0]
                index_from_note = self.notes_file.index('{}.pdf'.format(note))
                
                data_info_notes = {
                            "nameNote": self.notes_file[index_from_note],
                            "exist": "True"
                            }
                
                infos_note.append(data_info_notes)

                log.logger.info('Nota: {}.pdf do email: {} existe!'.format(note, email))

            except ValueError:
                
                self.verifyStatus = "False"

                data_info_notes = {
                                "nameNote": '{}.pdf'.format(note),
                                "exist": "False"
                            }
                
                infos_note.append(data_info_notes)

                space_line(100)
                print("ERRO - Nota {}.pdf do email: {}, nao foi encontrada, verifique a pasta PDF!".format(note, email))
                log.logger.error('Nota: {}.pdf do email: {} nao foi encontrada!'.format(note, email))

            except Exception as error:

                self.verifyStatus = "False"
                print('Algum erro desconhecido ocorreu ao verificar os arquivos de notas presente no diretório PDF, erro: {}, o programa será encerrado!'.format(error))
                log.logger.error('Algum erro desconhecido ocorreu ao verificar os arquivos de notas presente no diretório PDF, erro: {}'.format(error))

                sys.exit()

        if len(infos_note) > 0:

            dataStr = json.dumps(infos_note)

            self.cursor.execute(''' UPDATE Status SET nameNote = ? WHERE email = ?''', (dataStr, email))
            self.cursor.execute(''' UPDATE Status SET statusNote = ? WHERE email = ?''', (self.verifyStatus, email))

            self.conn.commit()