import sys
from networksecurity.logging.logger import logging


class NetSecException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f'Error occured in file {self.file_name} at line {self.lineno}. \
Error message: {str(self.error_message)}'


if __name__ == '__main__':
    logging.info('Entered exception file')
    try:
        a = 10/0
    except Exception as e:
        raise NetSecException(e, sys)
