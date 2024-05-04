from ..scriptDb.conn import Conect

class DefinedStatus:

    def __init__(self):

        conection = Conect()

        self.conn = conection.conn
        self.cursor = self.conn.cursor()
        
        self.get_status_files_and_set_status()

    def get_status_files_and_set_status(self):

        self.cursor.execute(''' UPDATE Status SET statusSend = ? WHERE statusBoleto = ? AND statusNote = ?''', (1, 'True', 'True'))
        self.cursor.execute(''' UPDATE Status SET statusSend = ? WHERE statusBoleto = ? OR statusNote = ?''', (0, 'False', 'False'))

        self.conn.commit()