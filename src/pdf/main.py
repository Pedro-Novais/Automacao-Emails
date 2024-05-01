import os

def verification_pdf():
    exi = 0
    dir_arq = ['Boletos', 'Notas']
    qnt_analysi = 0
    for indice_i in range(2):
        if(indice_i == 0):
            qnt_analysi = valor
        elif(indice_i == 1):
            qnt_analysi = valor_rep
        for i in range(len(qnt_analysi)):
            blt_not = []

            blt_not.append(qnt_analysi[i][1])
            blt_not.append(qnt_analysi[i][3])

            for ini in range(2):
                dir = f'../pdf/{dir_arq[ini]}/{blt_not[ini]}.pdf'
                if os.path.exists(dir):
                    print(f'{dir_arq[ini]}, de número {blt_not[ini]} existe')
                else:
                    print(f'{dir_arq[ini]}, de número {blt_not[ini]} não existe')
                    arq_falta.append([dir_arq[ini], blt_not[ini]])
                    exi = -1 
    return exi