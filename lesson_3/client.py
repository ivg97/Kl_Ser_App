'''
CLIENT
'''

import sys
import socket
import json


from additionally.constans import DEFAULT_PORT, DEFAULT_HOST
from additionally.func_client import client_presence, send_message_to_server, get_answer_from_server, parse_server_message

def start_client():

    try:
        HOST = sys.argv[2]
        PORT = int(sys.argv[3])
        if PORT < 1024 or PORT > 65535:
            raise ValueError
    except IndexError:
        HOST = DEFAULT_HOST
        PORT = DEFAULT_PORT
    except ValueError as err:
        print(f'Порт должен быть больше 1024 и менее 65535.')
        sys.exit(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    message_to_server = client_presence()
    send_message_to_server(sock, message_to_server)
    try:
        answer = parse_server_message(get_answer_from_server(sock))
        print(answer)
    except(ValueError, json.JSONDecodeError):
        print('Сообщение не разобрано')



if __name__ == '__main__':
    start_client()