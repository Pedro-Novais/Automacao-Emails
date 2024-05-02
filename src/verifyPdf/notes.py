import os
import json

class verifyNotes:

    def __init__(self, emails, cursor):

        self.conn = cursor

        self.cursor = cursor.cursor()

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

        note = self.notes[0][0]

        dir_relative = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

        dir_pdf_note = os.path.join(dir_relative, 'pdf', 'Notas', '{}.pdf'.format(note))

        if os.path.exists(dir_pdf_note):

            dataNote = {note: True}

            dataStr = json.dumps(dataNote)

            self.cursor.execute(''' UPDATE Status SET statusNote = ? WHERE email = ?''', (dataStr, email))

            self.conn.commit()

            print('Nota {} existe'.format(note))
        
        else:

            print('Nota {} nao existe'.format(note))