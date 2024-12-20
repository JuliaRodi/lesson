import os
import time
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file},\n '
              f'Путь: {file_path},\n '
              f'азмер: {file_size} байт,\n '
              f'Время изменения: {formatted_time},\n '
              f'Родительская директория: {parent_dir}')