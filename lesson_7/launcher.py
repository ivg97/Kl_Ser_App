import os
import subprocess
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
# PATH = os.path.join(PATH, 'client.log')
print(PATH)

process = []

while 1:
    action = input('q - exit, '
                   's - run,'
                   'x - close all window: ')
    if action == 'q':
        break
    elif action == 's':
        process.append(subprocess.Popen('gnome-terminal -- python3 server.py',
                                        shell=True))
        # for _ in range(2):
        #     process.append(subprocess.Popen('gnome-terminal -- '
        #                                     'python3 client.py -m send',
        #                                     shell=True))
        # for _ in range(2):
        #     process.append(subprocess.Popen('gnome-terminal -- '
        #                                     'python3 client.py -m listen',
        #                                     shell=True))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()
