"""Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
-имя файла без расширения или название каталога,
-расширение, если это файл,
-флаг каталога,
-название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование."""
import os
import logging
from collections import namedtuple


logging.basicConfig(filename='file_info.log', filemode='w', encoding='utf-8',
                    format='{levelname} - {asctime} : {msg}', style='{', level=logging.INFO)

logger = logging.getLogger(__name__)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'dir_flag', 'parent_dir'])


def get_file_info(dir_path):

    files_info = [(dirs, folders, files) for dirs, folders, files in os.walk(dir_path)]
    result = []
    for i in range(0, len(files_info)):
        parent_dir = files_info[i][0]
        dir_list = files_info[i][1]
        file_list = files_info[i][2]

        for el in dir_list:
            dir_flag = 'Yes'
            file_name = el
            file_exten = ''
            f = FileInfo(file_name, file_exten, dir_flag, parent_dir)
            result.append(f)
            logger.info(
                f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

        for item in file_list:
            dir_flag = 'No'
            try:
                file_name, file_exten = item.split('.')
            except Exception:
                *file_name, file_exten = item.split('.')

            f = FileInfo(file_name, file_exten, dir_flag, parent_dir)
            result.append(f)
            logger.info(
                f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')
    return result


# print(get_file_info('C:\\Users\\User\\Desktop'))
