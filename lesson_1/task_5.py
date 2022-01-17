'''
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
'''


import subprocess

data = ['ping', 'yandex.ru']

ping = subprocess.Popen(data, stdout=subprocess.PIPE)

for i in ping.stdout:
    print(i.decode('utf-8'))