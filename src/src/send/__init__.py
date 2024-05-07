from .constructorMessage import ConstructorMessage
from .verifyEmailsSend import VerifyEmailSend

class ExecSendEmail:

    def __init__(self):

        emails = VerifyEmailSend()

        for i in range(len(emails.emails)):

            ConstructorMessage(email=emails.emails[i][0])