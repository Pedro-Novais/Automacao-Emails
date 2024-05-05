from src.scriptDb.__init__ import execDatabase
from src.excel.__init__ import execGetValues
from src.insert.__init__ import execInsertData
from src.verifyPdf.__init__ import execNotes
from src.send.__init__ import ExecSendEmail

class execMain:

    def __init__(self):

        execDatabase()

        value = execGetValues()

        self.insertingValues(value.valueFinal, value.emails)

        self.verifyPdfs(emails=value.emails)

        ExecSendEmail()


    def insertingValues(self, values, emails):
        
        execInsertData(values, emails)

    def verifyPdfs(self, emails):

        execNotes(emails=emails)

execMain()