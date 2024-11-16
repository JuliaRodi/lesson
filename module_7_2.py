import io
from pprint import pprint

def custom_write(file_name: str, strings: list):#file_name - название файла для записи, strings - список строк для записи.
    strings_positions = {} #словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
                           # а значением - записываемая строка
    number_line = 1 # номер строки
    file = open(file_name, 'w', encoding = 'utf-8')
    for string in strings:
        line_byte = file.tell() # line_byte - байт начала строки
        file.write(f'{string}\n')
        strings_positions[(number_line, line_byte)] = string
        number_line += 1
    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)



