from .getData import getData

class execGetValues:

    def __init__(self):

        self.values = getData()

        self.valueFinal = self.values.value