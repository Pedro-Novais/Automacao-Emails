import openpyxl
import sys

class readExcel:

    def __init__(self):

        self.wb = self.read_excel()

    def read_excel(self):

        try:

            self = openpyxl.load_workbook('C:/New-Send-Email/excel/teste.xlsx')

            wb = self['TESTE']

        except Exception as e:

            print('')
            print("Erro ao realizar a leitura da planilha, verifique se o nome está correto: 'envio-faturamento.xlsx'")
            print(e)
            sys.exit()

        return wb