'''
Логирование клиента
'''

import sys
import logging
import os

# from ..additionally.constans import loggin_level

sys.path.append('../')


CLIENT_FORMAT = logging.Formatter('%(asctime)s %(levelname)s %(filename)s  %(message)s')
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')


stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(CLIENT_FORMAT)
stream_handler.setLevel(logging.DEBUG)
log_file = logging.FileHandler(PATH, encoding='utf-8')
log_file.setFormatter(CLIENT_FORMAT)


logger = logging.getLogger('client')
logger.addHandler(stream_handler)
logger.addHandler(log_file)
logger.setLevel(10)

if __name__ == '__main__':
    logger.critical('C')
    logger.error('E')
    logger.warning('W')
    logger.info('I')
    logger.debug('D')