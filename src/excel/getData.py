from .getExcel import readExcel

class getData:
    
    def __init__(self):

        self.value = self.get_value()

    def get_value(self):
         
        aba = readExcel()

        self = []
        i = 0

        for line in aba.wb:

            if i > 0:

                self.append([])
            
            for celula in line:

                posRow = celula.row
                valueBox = celula.value

                if posRow < 2:
                    i = 1

                if posRow > 1:

                    self[posRow - 2].append(valueBox)

        return self

    
    def get_email(self, values):

        self = []

        for i in range(len(values)):

            self.append(values[i][10])
        
        return self
