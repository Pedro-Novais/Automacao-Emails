from .notes import verifyNotes

class execNotes:

    def __init__(self, emails, cursor):

        verifyNotes(emails=emails, cursor = cursor)