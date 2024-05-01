from database.__init__ import execDatabase
from src.excel.__init__ import execGetValues
from src.insert.__init__ import execInsertData
from database.conn import Conect

class execMain:

    def __init__(self):

        execDatabase()

        value = execGetValues()

        self.insertingValues(value.valueFinal)

    def insertingValues(self, values):
        
        cursor = Conect()
        print(cursor.conn.cursor)
        execInsertData(values, cursor.conn)

execMain()