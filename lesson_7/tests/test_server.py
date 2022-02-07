'''
Unit-tests server
'''
import json
import unittest
from ..additionally.constans import RESPONSE, ERROR, TIME, USER, ACCOUNT_NAME, ACTION, PRESENCE, ENCODING
from ..additionally.func_server import forming_response_to_client, sending_response_to_client, receiving_client_messages


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


class TestServer(unittest.TestCase):
    '''
    Тестирование сервера
    '''

    message_no_action = {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}
    message_wrong_action = {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}
    message_no_time = {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}
    message_no_user = {ACTION: PRESENCE, TIME: '1.1'}
    message_unknown_user = {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}
    message_200_OK = {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}
    message_test_server = {
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

    def test_sending_response_to_client(self):
        '''Тест функции отправки сообщения'''
        sock = TestSocket(self.message_test_server)
        sending_response_to_client(sock, self.message_test_server)
        self.assertEqual(sock.encoded_message, sock.receved_message)
        with self.assertRaises(Exception):
            sending_response_to_client(sock, sock)

    def test_receiving_client_messages(self):
        '''Получени сообщения'''
        sock_ok = TestSocket(self.ok_dict)
        sock_err = TestSocket(self.err_dict)
        self.assertEqual(receiving_client_messages(sock_ok), self.ok_dict)
        self.assertEqual(receiving_client_messages(sock_err), self.err_dict)

    def test_forming_response_to_client_no_action(self):
        '''Отсутствие активности'''
        self.assertEqual(forming_response_to_client(self.message_no_action), self.err_dict)

    def test_forming_response_to_client_wrong_action(self):
        '''Неизвестное действие'''
        self.assertEqual(forming_response_to_client(self.message_wrong_action), self.err_dict)

    def test_forming_response_to_client_no_time(self):
        '''Потерялось время'''
        self.assertEqual(forming_response_to_client(self.message_no_time), self.err_dict)

    def test_forming_response_to_client_no_user(self):
        '''А где пользователь?'''
        self.assertEqual(forming_response_to_client(self.message_no_user), self.err_dict)

    def test_forming_response_to_client_unknown_user(self):
        '''Что за незвестный гость?'''
        self.assertEqual(forming_response_to_client(self.message_unknown_user), self.err_dict)

    def test_forming_response_to_client_200_OK(self):
        '''200 : OK'''
        self.assertEqual(forming_response_to_client(self.message_200_OK), self.ok_dict)


if __name__ == '__main__':
    unittest.main()
