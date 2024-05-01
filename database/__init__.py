from .models import CreateTable
from .conn import Conect

def execDatabase():
    
    table = CreateTable()

    create = table.createTable()

    if create:

        print('Tabela criadas com sucesso')
    else:
        print('Erro ao criar tabelas')
