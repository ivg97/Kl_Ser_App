'''
FUNCTIONS CLIENT
'''
import json
import time

from .constans import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, MAX_SIZE_SMS, \
    ENCODING


def client_presence(account_name='Guest'):
    result = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return result


def send_message_to_server(sock, message):
    message_json = json.dumps(message)
    encode_message = message_json.encode(ENCODING)
    sock.send(encode_message)

def get_answer_from_server(server):
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
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            # print(message[RESPONSE])
            return f'200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError