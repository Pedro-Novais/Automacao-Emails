from .notes import verifyNotes
from .blt import verifyBlt

class execNotes:

    def __init__(self, emails):

        verifyNotes(
            emails=emails
            )
        
        verifyBlt(
            emails=emails
            )