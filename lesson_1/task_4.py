'''
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
'''

words_list = [
    'разработка',
    'администрирование',
    'protocol',
    'standard',
]

def transfomation(words):
    for word in words:
        word_enc = word.encode('utf-8')
        word_dec = word_enc.decode('utf-8')
        print(f'{word}: {word_enc} - {word_dec}')


if __name__ == '__main__':
    transfomation(words_list)