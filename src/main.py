from src.scriptDb.__init__ import execDatabase
from src.excel.__init__ import execGetValues
from src.insert.__init__ import execInsertData
from src.verifyPdf.__init__ import execNotes
from src.send.__init__ import ExecSendEmail
from src.resetDatabase.__init__ import ExecResetDatabase
from src.verifyQuantityExecutions.__init__ import ExecVerifyQuantityExecution
from src.utils.verify_env import verify_env

class execMain:

    def __init__(self):

        verify_env()
        
        execDatabase()
        
        ExecVerifyQuantityExecution()

        value = execGetValues()

        self.insertingValues(value.valueFinal, value.emails)

        self.verifyPdfs(emails=value.emails)

        ExecSendEmail()

        ExecResetDatabase()


    def insertingValues(self, values, emails):
        
        execInsertData(values, emails)

    def verifyPdfs(self, emails):

        execNotes(emails=emails)

execMain()