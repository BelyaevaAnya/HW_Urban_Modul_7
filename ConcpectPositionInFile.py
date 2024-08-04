import io
from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r', encoding='utf-8')
print(file.writable())
print(file.readable())
print(file.seekable())
# False - записать не можем
# True - читать можем
# True - перемещать курсор можем
print(file.name)    # sample2.txt
print(file.buffer)  # <_io.BufferedReader name='sample2.txt'>
print(file.closed)  # False
print(file.tell())
pprint(file.read())
# file.seek(15)
# file.write('new text')
print(file.tell())
file.close()
# Ошибка кодировки(без параметра encoding)
# 0
# ('РџСЂРёРІРµС‚, СЏ РЅРѕРІС‹Р№ С‚РµРєСЃС‚\n'
#  'Р’С‚РѕСЂР°СЏ СЃС‚СЂРѕРєР° РЅРѕРІРѕРіРѕ С‚РµРєСЃС‚Р°')
# 91
# C параметром
# 0
# 'Привет, я новый текст\nВторая строка нового текста'
# 91