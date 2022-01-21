"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
from pprint import pprint

files_name = [
    'info_1.txt',
    'info_2.txt',
    'info_3.txt',
]

find_list = [
    'Изготовитель системы',
    'Название ОС',
    'Код продукта',
    'Тип системы',
]

name_fields = ['Название ОС, Код продукта, Изготовитель системы, Тип системы',]

def find_coincidence(words, line):
    result_list = ''
    for word in words:
        if line.find(word) == 0:
            result_list = line.split(word)[-1].replace(':', '').strip()
    if len(result_list) != 0:
        return result_list

def get_data(files, find_list):
    result = []
    result.append(name_fields)
    for file in files:
        l = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if find_coincidence(find_list, line) != None:
                    l.append(find_coincidence(find_list, line))

        result.append(l)
    return result
    # pprint(result)

def write_to_csv(file):
    data = get_data(files_name, find_list)
    with open(file, 'w') as f:
        f_write = csv.writer(f)
        for line in data:
            f_write.writerow(line)




if __name__ == '__main__':
    write_to_csv('data_report.csv')
