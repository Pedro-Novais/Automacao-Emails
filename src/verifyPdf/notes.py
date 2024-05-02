import os

class verifyNotes:

    def __init__(self, emails, cursor):

        self.conn = cursor

        self.cursor = cursor.cursor()

        self.verifyNotes(emails)

    def verifyNotes(self, emails):

        
        print(emails)