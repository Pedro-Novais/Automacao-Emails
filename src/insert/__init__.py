from .insertValues import Insert

class execInsertData:

    def __init__(self, value, conn):

        Insert(values=value, cursor=conn)