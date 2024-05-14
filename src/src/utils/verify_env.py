import os
import sys
from dotenv import load_dotenv
from .logs import Logs

def verify_env():

    try:

        log = Logs('Verification_File_env')

        load_dotenv()

        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')

        email_copy_one = os.getenv('EMAIL_COPY_ONE')
        email_copy_two = os.getenv('EMAIL_COPY_TWO')

        if email == "" or password == "":

            print('ERRO -  Preencha o arquivo .env, com suas informações de login para que o envio de email seja possível, o programa será encerrado!')
            log.logger.warning('Arquivo .env nao contem todos as informacoes para realizar o login e iniciar o envio de email')

            sys.exit()

        if email_copy_one == "" or email_copy_one == " " or email_copy_two == "" or email_copy_two == " ":

            print('ERRO -  Preencha o arquivo .env, com as infromações dos email copiados, o programa será encerrado!')
            log.logger.warning('Arquivo .env nao contem todos as informacoes dos emails copiados para realizar o envio!')

            sys.exit()

    except Exception as error:

        print('ERRO - Verify_env - Algum erro desconhecido ocorreu, erro: {}'.format(error))
        log.logger.error('Algum erro desconhecido ocorreu, erro: {}'.format(error))
        sys.exit()
