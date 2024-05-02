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

        try:
            self = []
            index_duplicated = []

            for i in range(len(values)):

                self.append(values[i][10])
            
            for i in range(len(self)):

                after = i + 1 

                if after >= len(self):

                    break

                if self[i] == self[after]:

                    index_duplicated.append(i)
            
            index_duplicated.reverse()

            for i in range(len(index_duplicated)):

                del self[index_duplicated[i]]

            return self
        
        except Exception as error:

            print('Erro na manipulação do email, {}'.format(error))