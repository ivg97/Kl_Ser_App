'''
CLIENT
'''

import sys
import socket
import json
import logging
from logs import client_log_config


from additionally.constans import DEFAULT_PORT, DEFAULT_HOST
from additionally.func_client import client_presence, send_message_to_server, get_answer_from_server, \
    parse_server_message
sys.path.append('../')


CLIENT_LOGGER = logging.getLogger('client')


def start_client():
    '''
    Запуск клиента
    :return:
    '''
    # Проверка указанного порта и адреса, инеаче по умолчанию
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
        CLIENT_LOGGER.critical(f'Запуск сервера на порту {sys.argv[3]} не допустимо. '
                               f'Допустимый диапазон портов от 1025 по 65535.')
        sys.exit(1)
    # Создание сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    CLIENT_LOGGER.info(f'Клиент запущен: {HOST}: {PORT}')
    # Подготовка сообщения для сервера
    message_to_server = client_presence()
    # Отправка сообщения серверу
    send_message_to_server(sock, message_to_server)
    try:
        # Получаем и разбираем сообщение о сервера
        answer = parse_server_message(get_answer_from_server(sock))
        CLIENT_LOGGER.info(f'Получено сообщение от сервера {answer}')
        print(answer)
    except(ValueError, json.JSONDecodeError):
        print('Сообщение не разобрано')
        CLIENT_LOGGER.error(f'Не удалось декорировать собщение от {sock}')


if __name__ == '__main__':
    start_client()
