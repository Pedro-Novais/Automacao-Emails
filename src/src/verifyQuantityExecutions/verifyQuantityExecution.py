import sys
from datetime import date
from ..scriptDb.conn import Conect
from ..utils.logs import Logs

class VerifyQuantityExecutions:

    def __init__(self):
        
        date_today = date.today()

        self.date = date_today.strftime('%Y-%m-%d')

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()

        self.log = Logs('Verify_Quantity_Executions')
        
        self.insert_date()

    def insert_date(self):
        
        try:
            self.cursor.execute('SELECT * FROM NumbersExecutes WHERE day = ?', (self.date,))

            line_in_table = self.cursor.fetchone()

            if line_in_table == None:

                self.cursor.execute(''' INSERT INTO NumbersExecutes 
                                    (day, quantityStartsBeforeComplete, complete) VALUES (?, ?, ?)
                                    ''', (self.date, 1, "False")
                                    )
                
                self.conn.commit()
                self.log.logger.info('Criação da linha, data {}, na tabela NumbersExecutes criada com sucesso'.format(self.date))

            else:
                
                if line_in_table[3] == "True":

                    while True:

                        ask_continue = input('ATENÇÃO - Uma planilha já foi enviada hoje, tem certeza que deseja realizar o envio de uma nova planilha? S/N: ')

                        response = self.resolve_ask(ask=ask_continue)

                        if response == True:
                            
                            self.log.logger.info('Confirmação de envio de uma nova planilha!')
                            print('ATENÇÃO - Garanta que os dados não sejam os mesmos, caso contrario, irá ocorrer a duplicidade de emails enviados!')
                            input('Pressione qualquer tecla para continuar...')
                        
                            break

                        else:
                            
                            self.log.logger.info('Cancelamento de envio de uma nova planilha!')
                            continue
                    
                    new_qty_after_complete = self.increment(line_in_table[4])

                    self.cursor.execute(''' UPDATE NumbersExecutes SET quantityAfterComplete = ? WHERE day = ? ''', (new_qty_after_complete, self.date) )
                    
                    self.conn.commit()

                    self.log.logger.info('Atualização da linha, data {}, na tabela NumbersExecutes realizada com sucesso, números de execução após o complete: {}'.format(self.date, new_qty_after_complete))

                else:
                    new_qty = self.increment(line_in_table[2])

                    self.cursor.execute(''' UPDATE NumbersExecutes SET quantityStartsBeforeComplete = ? WHERE day = ? ''', (new_qty, self.date) )
                    
                    self.conn.commit()

                    self.log.logger.info('Atualização da linha, data {}, na tabela NumbersExecutes realizada com sucesso, números de execução: {}'.format(self.date, new_qty))

        except Exception as error:

            print('ERRO - Verify_Quantity_Execution - Algum erro ocorreu ao criar/atualizar a linha, data {}, na tabela NumbersExecutes, erro: {}, o programa sera encerrado!'.format(error))
            self.log.logger.error('Algum erro ocorreu ao criar a linha, data {}, na tabela NumbersExecutes, erro: {}, o programa sera encerrado!'.format(error))
            sys.exit()

    @staticmethod
    def increment(qty):

        if qty == None:

            return 1
        
        new_qty = qty + 1

        return new_qty
    
    @staticmethod
    def resolve_ask(ask):

        if ask == "S" or ask == "s":

            return True
        
        elif ask == "N" or ask == "n":
            
            print('Ok, o programa será encerrado!')

            sys.exit()
        
        else: return False