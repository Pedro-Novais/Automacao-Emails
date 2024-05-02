from .insertValues import Insert

class execInsertData:

    def __init__(self, value, conn, emails):

        Insert(values=value, cursor=conn, emails=emails)