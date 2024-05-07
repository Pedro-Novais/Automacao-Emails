from .insertValues import Insert

class execInsertData:

    def __init__(self, value, emails):

        Insert(values=value, emails=emails)