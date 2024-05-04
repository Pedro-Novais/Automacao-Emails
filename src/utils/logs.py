import logging
import os

class Logs:

    def __init__(self, nameLog):

        dir_script = os.path.dirname(os.path.abspath(__file__))
        dir_log = os.path.abspath(os.path.join(dir_script, '..', '..', 'logs'))

        self.logger = logging.getLogger(nameLog)
        self.logger.setLevel(logging.INFO)

        self.handler = logging.FileHandler('{}/{}.log'.format(dir_log, nameLog))

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)