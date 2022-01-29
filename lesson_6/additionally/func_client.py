'''
FUNCTIONS CLIENT
'''
import json
import sys
import time
import logging
from lesson_6.decorators import log
sys.path.append('../')
import lesson_6.logs.client_log_config


from .constans import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, MAX_SIZE_SMS, \
    ENCODING



logger = logging.getLogger('client')


@log
def client_presence(account_name='Guest'):
    '''
    Проверка присутствя клиента и подготовка сообщения
    :param account_name:
    :return:
    '''
    result = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    logger.info(f'Сообщение подготовлено')
    return result

@log
def send_message_to_server(sock, message):
    '''
    Отправить сообщение на сервер
    :param sock:
    :param message:
    :return:
    '''
    message_json = json.dumps(message)
    encode_message = message_json.encode(ENCODING)
    try:
        sock.send(encode_message)
    except Exception:
        logger.error(f'Сообщение {message} не отправлено.')


@log
def get_answer_from_server(server):
    '''
    Получить ответ от сервера
    :param server:
    :return: 200 : OK
    '''
    response = server.recv(MAX_SIZE_SMS)
    if isinstance(response, bytes):
        response_json = response.decode(ENCODING)
        response = json.loads(response_json)
        if isinstance(response, dict):
            # print(response)
            return response
        raise ValueError
    raise ValueError


@log
def parse_server_message(message):
    '''
    Разбор ответа (сообщения) сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            # print(message[RESPONSE])
            return f'200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError