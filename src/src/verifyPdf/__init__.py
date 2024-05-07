from .notes import VerifyNotes
from .blt import VerifyBlt
from .definedStatusFinal import DefinedStatus

class execNotes:

    def __init__(self, emails):

        VerifyNotes(
            emails=emails
            )
        
        VerifyBlt(
            emails=emails
            )
        
        DefinedStatus()