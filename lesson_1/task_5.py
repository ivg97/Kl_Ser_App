'''
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
'''


import subprocess
import urllib.request, chardet

data = ['ping', 'yandex.ru']

ping = subprocess.Popen(data, stdout=subprocess.PIPE)

ur = urllib.request.urlopen('http://yandex.ru/').read()
print(chardet.detect(ur))

for i in ping.stdout:
    print(i.decode('utf-8'))




