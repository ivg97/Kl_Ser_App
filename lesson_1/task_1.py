'''
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и
содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
'''


words_list_str = ['разработка', 'сокет', 'декоратор', ]

words_list_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                      '\u0441\u043e\u043a\u0435\u0442',
                      '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440', ]



def str_format_type(lst_str, lst_unicode):
    for i in lst_str:
        print(f'{i} - {type(i)}')
    for j in lst_unicode:
        print(f'{j} - {type(i)}')


str_format_type(words_list_str, words_list_unicode)


if __name__ == '__main__':
    str_format_type(words_list_str, words_list_unicode)