from pprint import pprint


def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file_obj:
        file_dict = {}
        for ind, str_wr in enumerate(strings, start=1):
            cursor_pos = file_obj.tell()
            file_obj.write(f'{str_wr}\n')
            file_dict.update({(ind, cursor_pos): str_wr})
    return file_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
