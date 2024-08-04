from pprint import pprint
# Режимы открытия файлов python
# r - read
# w - write
# a - append
# если файл бинарны то добавлем к ним букву b
name = 'sample.txt'
file = open(name, 'r')
print(file)
# Читаем содержимое
pprint(file.read())
# Закрываем файл
file.close()
name = 'sample2.txt'
file = open(name, 'w')
file.write('hi>sadas')
file.close()
file = open(name, 'r')
print(file.read())
file = open(name, 'a')
file.write('\nHello2\n')
file.close()
file = open(name, 'r')
print(file.read())
file.close()
# cursor
file = open(name, 'r')
print(file.tell())
print(file.read())
print(file.seek(9))
print(file.read())
print(file.tell())

file.close()
