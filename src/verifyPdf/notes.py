import os
import json
import logging
from ..utils.getFiles import getFiles
from ..scriptDb.conn import Conect

class verifyNotes:

    def __init__(self, emails):

        self.logs()

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        #self.conn = cursor

        #self.cursor = cursor.cursor()

        self.notes_file = getFiles('Notas')

        self.verify(emails)

    def verify(self, emails):

        for i in range(len(emails)):
            
            self.getNoteSave(emails[i])
                
            self.verifyNotesFiles(emails[i])

    def getNoteSave(self, email):

        try:
            
            self.cursor.execute(''' SELECT notes FROM Emails WHERE email = ?''', (email,))

            self.notes = self.cursor.fetchall()
        
        except Exception as error:

            print(error)

    def verifyNotesFiles(self, email):

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

                self.logger.info('Nota: {}.pdf do email: {} existe!'.format(note, email))

            except ValueError:
                
                self.verifyStatus = "False"

                data_info_notes = {
                                "nameNote": '{}.pdf'.format(note),
                                "exist": "False"
                            }
                
                infos_note.append(data_info_notes)

                print("Nota {}.pdf do email: {}, não encontrada no diretório de arquivos PDF".format(note, email))
                self.logger.error('Nota: {}.pdf do email: {} nao existe!'.format(note, email))

            except Exception as error:

                self.verifyStatus = "False"
                print(error)
                self.logger.error('Algum erro desconhecido ocorreu: {}'.format(error))

                break

        if len(infos_note) > 0:

            dataStr = json.dumps(infos_note)

            self.cursor.execute(''' UPDATE Status SET nameNote = ? WHERE email = ?''', (dataStr, email))
            self.cursor.execute(''' UPDATE Status SET statusNote = ? WHERE email = ?''', (self.verifyStatus, email))

            self.conn.commit()

    def logs(self):

        dir_script = os.path.dirname(os.path.abspath(__file__))
        dir_log = os.path.abspath(os.path.join(dir_script, '..', '..', 'logs'))

        self.logger = logging.getLogger('notes')
        self.logger.setLevel(logging.INFO)

        self.handler = logging.FileHandler('{}/note.log'.format(dir_log))

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)