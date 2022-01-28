'''
FUNCTIONS CLIENT
'''
import json
import sys
import time
import logging
sys.path.append('../')
import lesson_5.logs.client_log_config


from .constans import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, MAX_SIZE_SMS, \
    ENCODING



CLIENT_LOGGER = logging.getLogger('client')



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
    CLIENT_LOGGER.info(f'Сообщение подготовлено')
    return result


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
        CLIENT_LOGGER.error(f'Сообщение {message} не отправлено.')

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