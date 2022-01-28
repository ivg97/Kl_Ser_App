'''
Определить, какие из слов «attribute», «класс», «функция», «функция» невозможно записать в байтовом типе.
'''

words_list = [
    'attribute',
    'класс',
    'функция',
    'функция',
]


def type_b(words):
    for word in words:
        try:
            print(f'{word} - {bytes(word, "ascii")}')
        except UnicodeEncodeError as err:
            print(f'{word}  невозможно записать в байтовом типе')


if __name__ == '__main__':
    type_b(words_list)