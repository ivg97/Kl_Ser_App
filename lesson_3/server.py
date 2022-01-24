'''
SERVER
'''
import json
import socket
import sys

from additionally.constans import DEFAULT_PORT, DEFAULT_HOST, QUANTITY_CONNECTION
from additionally.func_server import receiving_client_messages, forming_response_to_client, sending_response_to_client


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
        sys.exit(1)
    except ValueError:
        print(f'Порт не может быть меньше 1024 и больше 65535')
        sys.exit(1)

    # Проверка указанного адреса, иначе по умолчанию
    try:
        if '-a' in sys.argv:
            HOST = sys.argv[sys.argv.index('-a') +1]
        else:
            HOST = DEFAULT_HOST
    except IndexError:
        print(f'Укажите адрес после параметра -\'a\'')
        sys.exit(1)

    # Создание сокета
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(QUANTITY_CONNECTION)
        while True:
            client, addr = sock.accept()
            try:
                # Прием сообения от клиента
                client_message = receiving_client_messages(client)
                print(client_message)
                # Формирование ответа клиенту
                response = forming_response_to_client(client_message)
                # Отправка сообщения клиенту
                sending_response_to_client(client, response)
                client.close()
            except(ValueError, json.JSONDecodeError):
                print(f'Сообщение клиента не корректно')
                client.close()




if __name__ == '__main__':
    start_server()