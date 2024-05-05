import smtplib
import ssl
import os
import sys
from ..utils.logs import Logs
from smtplib import SMTPAuthenticationError
from ..scriptDb.conn import Conect
from dotenv import load_dotenv

class ConectServer:

    def __init__(self, destinatary, msg):

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        try:
            # destinatary = "phnovais7@gmail.com"
            log = Logs('Conect_smtp')
            
            load_dotenv()

            smtp_server = 'smtp.office365.com'
            smtp_port = 587  # Porta TLS padrão
            smtp_username = os.getenv('EMAIL')
            smtp_password = os.getenv('PASSWORD')

            # Criar uma conexão SMTP segura com SSL/TLS
            context = ssl.create_default_context()

            with smtplib.SMTP(smtp_server, smtp_port) as server:

                server.starttls(context=context)  # Inicia a criptografia TLS
                server.login(smtp_username, smtp_password)  # Autentica-se com o servidor SMTP

                log.logger.info('Login realizado com sucesso no servidor smtp')

                server.sendmail(os.getenv('EMAIL'), destinatary, msg.as_string())

                print('Email enviado com sucesso para {}'.format(destinatary))
                log.logger.info('Email enviado com sucesso para {}'.format(destinatary))
            
            self.cursor.execute(''' UPDATE Status SET sended = ? WHERE email = ?''', ("True", destinatary))

            self.conn.commit()

            sys.exit()
        except SMTPAuthenticationError as error:

            print('Credenciais para realizar login está incorreta, verifique o arquivo .env, erro: {}'.format(error))
            log.logger.error('Erro ao realizar login no servidor smtp, credenciais inválidas, {}'.format(error))
        
        except Exception as error:

            print('ERRO - Algum erro inesperado ocorreu ao realizar o login no servidor smtp, erro: {}'.format(error))
            log.logger.error('Algum erro inesperado ocorreu ao realizar o login no servidor smtp, erro: {}'.format(error))