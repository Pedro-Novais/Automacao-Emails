import os
import sys
from ..utils.logs import Logs

def getFiles(type):

    log = Logs('Get_Files')

    try:
        dir_relative = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

        dir = os.path.join(dir_relative, 'pdf', '{}'.format(type))

        if os.path.exists(dir):

            files = os.listdir(dir)

            if files:
                
                log.logger.info('Arquivos PDF encontrados na pasta {} e retornados com sucesso'. format(dir))
                
                return files
            
            else:

                print('Nenhum arquivo pdf encontrado no diretório: {}'.format(dir))
                log.logger.warning('Nenhum arquivo PDF foi encontrado no diretório: {}'.format(dir))
                
                sys.exit()
        
        else:

            print('Diretório {} não encontrado, verifique e tente-o novamente'.format(dir))
            log.logger.warning('Diretório {} não foi encontrado'.format(dir))

            sys.exit()

    except Exception as error:

        print('Algum erro inesperado ocorreu ao tentar localizar os arquivos PDF, erro: {}, o programa será encerrado'.format(error))
        log.logger.error('Algum erro inesperado ocorreu ao tentar localizar os arquivos PDF, erro: {}'.format(error))

        sys.exit()