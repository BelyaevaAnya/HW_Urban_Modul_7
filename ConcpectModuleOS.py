import os

print('Текущая директория: ', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директория: ', os.getcwd())
# os.makedirs(r'third\fourth')
print(os.listdir())
# for i in os.walk('.'):
#     print(i)
os.chdir(r'C:\Users\belae\PycharmProjects\HW_Urban_Modul_7\Mother Goose - Monday’s Child')
print('Текущая директория: ', os.getcwd())
print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(file)
print(dirs)
# os.startfile(file[2]) запуск файла
print(os.stat(file[2]))
print(os.stat(file[2]).st_mtime)
print(os.stat(file[2]).st_size)
os.system('pip install random2')