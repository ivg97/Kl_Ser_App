'''
Декораторы для сервера и клиента
'''


import sys
import logging
import logs.client_log_config
import logs.server_log_config

if sys.argv[0].split('/')[-1] == 'client.py':
    logger = logging.getLogger('client')
else:
    logger = logging.getLogger('server')


def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)

        logger.debug(f'Функция {func.__name__}:'
                     f'args - {args};'
                     f'kwargs = {kwargs}')
        return res
    return wrapper
