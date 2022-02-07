'''
CLIENT
'''

import sys
import socket
import json
import logging
from decorators import log
from logs import client_log_config


from additionally.constans import DEFAULT_PORT, DEFAULT_HOST, ACTION, SENDER, \
    MESSAGE_TEXT
from additionally.func_client import client_presence, send_message_to_server, \
    get_answer_from_server, parse_server_message, create_message

sys.path.append('../')

@log
def message_from_server(message):
    """Функция - обработчик сообщений других пользователей, поступающих с сервера"""
    if ACTION in message and message[ACTION] == 'message' and \
            SENDER in message and MESSAGE_TEXT in message:
        print(f'Получено сообщение от пользователя '
              f'{message[SENDER]}:\n{message[MESSAGE_TEXT]}')
        logger.info(f'Получено сообщение от пользователя '
                    f'{message[SENDER]}:\n{message[MESSAGE_TEXT]}')
    else:
        logger.error(f'Получено некорректное сообщение с сервера: {message}')

logger = logging.getLogger('client')


# print(sys.argv[2])

@log
def start_client():
    '''
    Запуск клиента
    :return:
    '''

    try:
        if '-m' in sys.argv:
            flag_client = sys.argv[sys.argv.index('-m') +1]
        else:
            flag_client = 'listen'
    except IndexError:
        print(f'Укажите номер порта после параметра -\'m\'')
        logger.critical(f'Не указано значение после параметра -m.')
        sys.exit(1)
    if flag_client not in ('listen', 'send'):
        logger.critical(f'Указан недопустимый режим {flag_client}'
                        f'Допустимые режимы: listen, send')

    # Проверка указанного порта и адреса, инеаче по умолчанию

    try:
        if '-m' not in sys.argv:

            HOST = sys.argv[2]
            PORT = int(sys.argv[3])
        else:
            HOST = DEFAULT_HOST
            PORT = DEFAULT_PORT

        if PORT < 1024 or PORT > 65535:
            raise ValueError
    except IndexError:
        HOST = DEFAULT_HOST
        PORT = DEFAULT_PORT
    except ValueError as err:
        print(f'Порт должен быть больше 1024 и менее 65535.')
        logger.critical(f'Запуск сервера на порту {sys.argv[3]} не допустимо. '
                               f'Допустимый диапазон портов от 1025 по 65535.')
        HOST = DEFAULT_HOST
        PORT = DEFAULT_PORT
        # sys.exit(1)
    # Создание сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    logger.info(f'Клиент запущен: {HOST}: {PORT}')
    # Подготовка сообщения для сервера
    # message_to_server = client_presence()
    # Отправка сообщения серверу
    # send_message_to_server(sock, message_to_server)
    # try:
        # Получаем и разбираем сообщение о сервера
        # answer = parse_server_message(get_answer_from_server(sock))
        # logger.info(f'Получено сообщение от сервера {answer}')
        # print(answer)
    # except(ValueError, json.JSONDecodeError):
    #     print('Сообщение не разобрано')
    #     logger.error(f'Не удалось декорировать собщение от {sock}')
    while True:
        if flag_client == 'send':
            print(f'Режим работы - отправка сообщений')
        else:
            print(f'Режим работы - прием сообщений')
        while True:
            if flag_client == 'send':
                try:
                    send_message_to_server(sock, create_message(sock))
                except (ConnectionResetError, ConnectionError,
                        ConnectionAbortedError) as err:
                    logger.error(f'Соединение потеряно. Причина: {err}')
                    sys.exit(1)
            if flag_client == 'listen':
                try:
                    message_from_server(get_answer_from_server(sock))
                except (ConnectionResetError, ConnectionError,
                        ConnectionAbortedError) as err:
                    logger.error(f'Соединение потеряно. Причина: {err}')
                    sys.exit(1)


if __name__ == '__main__':
    start_client()
