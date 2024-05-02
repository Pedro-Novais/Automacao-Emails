from .getData import getData

class execGetValues:

    def __init__(self):

        self.values = getData()

        self.valueFinal = self.values.value

        self.emails = self.values.get_email(self.valueFinal)