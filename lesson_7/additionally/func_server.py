'''
FUNCTION SERVER
'''
import json
import logging
from lesson_6.decorators import log
from .constans import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR, ENCODING, MAX_SIZE_SMS, MESSAGE_TEXT

from lesson_6.logs import server_log_config

logger = logging.getLogger('server')

@log
def receiving_client_messages(client):
    '''
    Принимет сообщения от клиента
    :return:
    '''

    encode_response = client.recv(MAX_SIZE_SMS)
    if isinstance(encode_response, bytes):
        response_json = encode_response.decode(ENCODING)
        response = json.loads(response_json)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


@log
def forming_response_to_client(message, message_list, client):
    '''
    Формирует ответ для клиента
    :return:
    '''
    logger.debug(f'Разбор сообщения {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        sending_response_to_client(client, {RESPONSE: 200})
        return
    elif ACTION in message and message[ACTION] == 'message' and TIME in \
        message and MESSAGE_TEXT in message:
        message_list.append((message[ACCOUNT_NAME], message[MESSAGE_TEXT]))
        return
    logger.warning(f'Возвращен статус 400.')
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

@log
def sending_response_to_client(client, answer):
    '''
    Отправка ответа клиенту
    :return:
    '''
    answer_json = json.dumps(answer)
    encode_answer = answer_json.encode(ENCODING)
    client.send(encode_answer)

