import os
import json
import logging
from ..utils.getFiles import getFiles

class verifyNotes:

    def __init__(self, emails, cursor):

        self.logs()

        self.conn = cursor

        self.cursor = cursor.cursor()

        self.notes_file = getFiles('Notas')

        self.verifyNotes(emails)

    def verifyNotes(self, emails):

        for i in range(len(emails)):
            
            self.getNote(emails[i])

            if len(self.notes) == 1:
                
                self.verifyOneNote(emails[i])
            
            elif len(self.notes) > 1:
                print('legal')

    def getNote(self, email):

        try:
            
            self.cursor.execute(''' SELECT notes FROM Emails WHERE email = ?''', (email,))

            self.notes = self.cursor.fetchall()

            print(self.notes)
        
        except Exception as error:

            print(error)
    
    def verifyOneNote(self, email):

        try:
            note = self.notes[0][0]

            index_from_note = self.notes_file.index('{}.pdf'.format(note))

            infos_note = {
                            "nameNote": self.notes_file[index_from_note],
                            "exist": "True"
                          }
            
            dataNote = [infos_note]

            dataStr = json.dumps(dataNote)

            self.cursor.execute(''' UPDATE Status SET statusNote = ? WHERE email = ?''', ("True", email))
            self.cursor.execute(''' UPDATE Status SET nameNote = ? WHERE email = ?''', (dataStr, email))

            self.conn.commit()

            self.logger.info('Nota: {}.pdf do email: {} existe!'.format(note, email))
        
        except ValueError:
            
            infos_note = {
                            "nameNote": '{}.pdf'.format(note),
                            "exist": "False"
                          }
            
            dataNote = [infos_note]

            dataStr = json.dumps(dataNote)

            self.cursor.execute(''' UPDATE Status SET statusNote = ? WHERE email = ?''', ("False", email))
            self.cursor.execute(''' UPDATE Status SET nameNote = ? WHERE email = ?''', (dataStr, email))

            self.conn.commit()

            print("Nota {}.pdf do email: {}, não encontrada no diretório de arquivos PDF".format(note, email))
            self.logger.error('Nota: {}.pdf do email: {} nao existe!'.format(note, email))

        except Exception as error:

            print(error)
            self.logger.error('Algum erro inesperado ocorreu - {}'.format(error))

            return False

    def logs(self):

        self.dir_script = os.path.dirname(os.path.abspath(__file__))

        self.logger = logging.getLogger('notes')
        self.logger.setLevel(logging.INFO)

        self.handler = logging.FileHandler('{}/note.log'.format(self.dir_script))

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)