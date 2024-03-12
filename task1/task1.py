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

    files_info = []
    for root, dirs, files in os.walk(dir_path):
        for item in dirs:
            files_info.append(FileInfo(name=item, extension=None, dir_flag=True, parent_dir=root))
            logger.info(f'{item}, {None}, {True}, {root}')
        for item in files:
            name, ext = os.path.splitext(item)
            files_info.append(FileInfo(name=name, extension=ext, dir_flag=False, parent_dir=root))
            logger.info(f'{name}, {ext}, {False}, {root}')
    return files_info


print(get_file_info('C:\\Users\\User\\Desktop\\Участок'))
