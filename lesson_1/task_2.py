'''
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''


words_list = [
    b'class',
    b'function',
    b'method',
]

def transformation_in_bt(worlds):
    for word in worlds:
        print(f'{word} - {type(word)}')



if __name__ == '__main__':
    transformation_in_bt(words_list)
