'''
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
 «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате
 Unicode и вывести его содержимое.
'''
import locale

words_list = [
    'сетевое программирование',
    'сокет',
    'декоратор',
]
with open('test_file.txt', 'w') as f:
    for word in words_list:
        f.write(word + '\n')

print(locale.getpreferredencoding())

with open('test_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(f'{line.strip()}')