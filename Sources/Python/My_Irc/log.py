import logging
import time
import os

class Log:

    def __init__(self,path):
        LOG_FILENAME = os.path.join(path)
        logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

    def write_info(self,msg):
        logging.info(msg)

    def write_warning(self,msg):
        logging.warning(msg)

    def write_error(self,msg):
        logging.error(msg)

    def write_critical(self,msg):
        logging.critical(msg)

