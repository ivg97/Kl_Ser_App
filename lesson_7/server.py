'''
SERVER
'''

import socket
import sys
import logging
import select
import time

from logs import server_log_config
from decorators import log
from additionally.constans import DEFAULT_PORT, DEFAULT_HOST, \
    QUANTITY_CONNECTION, ACTION, SENDER, TIME, MESSAGE_TEXT
from additionally.func_server import receiving_client_messages, \
    forming_response_to_client, sending_response_to_client



logger = logging.getLogger('server')


@log
def start_server():
    '''
    Запуск сервера
    :return:
    '''

    # Проверка указанного порта, иначе по умолчанию
    try:
        if '-p' in sys.argv:
            PORT = int(sys.argv[sys.argv.index('-p') +1])
        else:
            PORT = DEFAULT_PORT
        if PORT < 1024 or PORT > 65535:
            raise ValueError
    except IndexError:
        print(f'Укажите номер порта после параметра -\'p\'')
        logger.critical(f'Не указано значение после параметра -р.')
        sys.exit(1)
    except ValueError:
        print(f'Порт не может быть меньше 1024 и больше 65535')
        logger.critical(f'Указан недопустимый номер порта. '
                               f'Диапазон допустимых портов с 1025 по 65535')
        sys.exit(1)

    # Проверка указанного адреса, иначе по умолчанию
    try:
        if '-a' in sys.argv:
            HOST = sys.argv[sys.argv.index('-a') +1]
        else:
            HOST = DEFAULT_HOST
    except IndexError:
        print(f'Укажите адрес после параметра -\'a\'')
        logger.critical(f'Не указано значение после параметра -а.')
        sys.exit(1)

    # клиенты и сообщения
    clients = []
    messages = []

    # Создание сокета
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.settimeout(1.5)
        sock.listen(QUANTITY_CONNECTION)

        while True:
            try:
                client, addr = sock.accept()
            except OSError as err:
                print('73 string', err)
            else:
                logger.info(f'Установлено соединение с ПК {addr}')
                clients.append(client)

            get_data_list = []
            send_data_list = []

            print('dict', get_data_list, send_data_list)

            try:
                if clients:
                    get_data_list, send_data_list, error_list = select.select(
                        clients, clients, [], 0
                    )
            except OSError as err:
                print('88 string', err)

            if get_data_list:
                for message_client in get_data_list:
                    try:
                        forming_response_to_client(receiving_client_messages(
                            message_client), messages, message_client)
                    except:
                        logger.info(f'Клиент oтключился')
                        clients.remove(message_client)
            if messages in send_data_list:
                messages = {
                    ACTION: 'message',
                    SENDER: messages[0][0],
                    TIME: time.time(),
                    MESSAGE_TEXT: messages[0][1],
                }
                del messages[0]

                for client_waiting in send_data_list:
                    try:
                        sending_response_to_client(client_waiting, messages)
                    except:
                        logger.info('Клиент отключился!')
            # try:
            #     # Прием сообения от клиента
            #     client_message = receiving_client_messages(client)
            #     logger.debug(f'Принято сообщение {client_message}')
            #     print(client_message)
            #     # Формирование ответа клиенту
            #     response = forming_response_to_client(client_message)
            #     logger.debug(f'Ответ клиенту сформирован {response}')
            #     # Отправка сообщения клиенту
            #     sending_response_to_client(client, response)
            #     client.close()
            # except(ValueError, json.JSONDecodeError):
            #     logger.error(f'Клиент {addr} отправил некорректное сообщение.')
            #     print(f'Сообщение клиента не корректно')
            #     client.close()




if __name__ == '__main__':
    start_server()