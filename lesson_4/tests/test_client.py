'''
Unit-tests server
'''
import json
import unittest

from lesson_4.additionally.constans import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, ENCODING
from lesson_4.additionally.func_client import client_presence, parse_server_message, send_message_to_server, \
    get_answer_from_server


class TestSocket:
    def __init__(self, test_mes):
        self.test_mes = test_mes
        self.encoded_message = None
        self.receved_message = None

    def send(self, message):
        json_message = json.dumps(self.test_mes)
        self.encoded_message = json_message.encode(ENCODING)
        self.receved_message = message

    def recv(self, len):
        json_messages = json.dumps(self.test_mes)
        return json_messages.encode(ENCODING)


class TestClient(unittest.TestCase):
    '''Тестирование клиента'''

    messages_OK = {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}
    message_test_client = {
        ACTION: PRESENCE,
        TIME: 10.1,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}


    def test_send_message_to_server(self):
        '''Отправка сообщения серверу'''
        sock = TestSocket(self.message_test_client)
        send_message_to_server(sock, self.message_test_client)
        self.assertEqual(sock.encoded_message, sock.receved_message)
        with self.assertRaises(Exception):
            send_message_to_server(sock, sock)


    def test_get_answer_from_server(self):
        '''Получение сообщения от сервера'''
        sock_ok = TestSocket(self.ok_dict)
        sock_err = TestSocket(self.err_dict)
        self.assertEqual(get_answer_from_server(sock_ok), self.ok_dict)
        self.assertEqual(get_answer_from_server(sock_err), self.err_dict)


    def test_create_presence(self):
        '''Корректный запрос сообщения'''
        client_pres = client_presence()
        client_pres[TIME] = 1.1
        self.assertEqual(client_pres, self.messages_OK)

    def test_parse_server_message_200(self):
        '''Тест 200 : OK'''
        self.assertEqual(parse_server_message(self.ok_dict), '200 : OK')

    def test_parse_server_message_400(self):
        '''Тест 400'''
        self.assertEqual(parse_server_message(self.err_dict), '400 : Bad Request')

    def test_exc(self):
        '''Тест исключения'''
        with self.assertRaises(ValueError):
            parse_server_message({ERROR: 'Bad Request'})