import os

def getFiles(type):

    dir_relative = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    dir = os.path.join(dir_relative, 'pdf', '{}'.format(type))

    if os.path.exists(dir):

        files = os.listdir(dir)

        if files:

            return files
        
        else:

            print('Nenhum arquivo pdf encontrado no diretório: {}'.format(dir))

            return False
    
    else:

        print('Diretório {} não encontrado'.format(dir))

        return False