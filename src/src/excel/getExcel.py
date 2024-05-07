import openpyxl
import sys
import os
from ..utils.logs import Logs

class readExcel:

    def __init__(self):

        self.wb = self.read_excel()

    def read_excel(self):

        try:
            log = Logs('Get_Excel')

            dir_relative = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'excel', 'faturamento.xlsx'))

            self = openpyxl.load_workbook(dir_relative)

            wb = self['FATURAMENTO']

            log.logger.info('Leitura da planilha realizada com sucesso')

        except FileNotFoundError as error:

            print("Planilha nao foi identificada na pasta Excel, verifique se o nome esta correto: faturamento.xlsx")
            log.logger.error('Planilha não foi identificada na pasta Excel, verifique se o nome está correto: faturamento.xlsx", erro: {}'.format(error))
            sys.exit()

        except Exception as error:
            
            if str(error.args[0]) == "Worksheet FATURAMENTO does not exist.":

                print("ERRO - Verifique se a aba da planilha está com o nome correto: FATURAMENTO, todos os caracteres deve estar em maiusculo, o programa será encerrado!")
                log.logger.error('Aba da planilha não foi encontrada, verifique se o nome está correto: FATURAMENTO, erro: {}'.format(error))
                sys.exit()
            
            else:
                print("Algum erro inesperado ocorreu, {}, o programa será encerrado".format(error))
                log.logger.error('Algum erro inesperado ocorreu, erro: {}'.format(error))
                sys.exit()

        return wb