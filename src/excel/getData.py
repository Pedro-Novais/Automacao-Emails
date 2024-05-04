import sys
from .getExcel import readExcel
from ..utils.logs import Logs

class getData:
    
    def __init__(self):

        self.value = self.get_value()

    def get_value(self):
        
        log = Logs('Get_Values')
        aba = readExcel()

        self = []
        i = 0

        try: 
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

        except Exception as error:

            print('Algum erro inesperado ocorreu ao selecionar os valores da planilha, erro: {}'.format(error))
            log.logger.error('Algum erro inesperado ocorreu ao selecionar os valores da planilha, erro: {}'.format(error))
            sys.exit()

        log.logger.info('Todos os valores da planilha foram selecionados com sucesso')

        return self

    def get_email(self, values):

        log = Logs('Get_email')

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

            log.logger.info("Email's selecionados com sucesso")
            
            return self
        
        except Exception as error:

            print('Ocorreu algum erro ao realizar a manipulação dos emails, erro: {}'.format(error))
            log.logger.error('Ocorreu algum erro ao realizar a manipulação dos emails, erro: {}'.format(error))
            sys.exit()