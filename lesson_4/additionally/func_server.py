'''
FUNCTION SERVER
'''
import json

from .constans import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, ENCODING, MAX_SIZE_SMS


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



def forming_response_to_client(message):
    '''
    Формирует ответ для клиента
    :return:
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def sending_response_to_client(client, answer):
    '''
    Отправка ответа клиенту
    :return:
    '''
    answer_json = json.dumps(answer)
    encode_answer = answer_json.encode(ENCODING)
    client.send(encode_answer)

