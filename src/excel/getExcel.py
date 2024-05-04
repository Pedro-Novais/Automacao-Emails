import openpyxl
import sys
from ..utils.logs import Logs

class readExcel:

    def __init__(self):

        self.wb = self.read_excel()

    def read_excel(self):

        try:
            log = Logs('Excel')

            self = openpyxl.load_workbook('C:/New-Send-Email/excel/teste.xlsx')

            wb = self['FATURAMENTO']

            log.logger.info('Leitura da planilha realizada com sucesso')

        except FileNotFoundError as error:

            print("Planilha nao foi identificada na pasta Excel, verifique se o nome esta correto: envio-faturamento.xlsx")
            log.logger.error('Planilha não foi identificada na pasta Excel, verifique se o nome está correto: envio-faturamento.xlsx", erro: {}'.format(error))
            sys.exit()

        except Exception as error:

            print("Algum erro inesperado ocorreu, {}".format(error))
            log.logger.error('Algum erro inesperado ocorreu, erro: {}'.format(error))
            sys.exit()

        return wb