from pprint import pprint

name = 'sample2.txt'
# with EXPR as TARG:
#     ACTION
with open(name, encoding='utf-8') as file:
    for line in file:
        for char in file:
            print(char, end='')
    print(file.tell())
