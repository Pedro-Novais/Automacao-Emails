from database.__init__ import execDatabase
from src.excel.__init__ import execGetValues
from src.insert.__init__ import execInsertData
from src.verifyPdf.__init__ import execNotes
from database.conn import Conect

class execMain:

    def __init__(self):

        execDatabase()

        value = execGetValues()

        self.insertingValues(value.valueFinal, value.emails)

        self.verifyPdfs(emails=value.emails)


    def insertingValues(self, values, emails):
        
        cursor = Conect()
        execInsertData(values, cursor.conn, emails)

    def verifyPdfs(self, emails):

        cursor = Conect()
        execNotes(emails=emails, cursor=cursor.conn)

execMain()