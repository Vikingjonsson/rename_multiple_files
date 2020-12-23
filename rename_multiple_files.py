#!/usr/bin/python3
import sys
import os
from typing import List, Final


def get_folder_content(path: str = '') -> List[str]:
    return os.listdir(path) if path else []


def get_files_in_folder(path: str = '') -> List[str]:
    FOLDER_CONTENT: Final = get_folder_content(path)
    return [os.path.join(path, file) for file in FOLDER_CONTENT if os.path.isfile(os.path.join(path, file))]


def rename_file(file_path: str = '', pattern: str = '', new_name: str = '') -> None:
    path, file_name = os.path.split(file_path)

    if pattern and pattern in file_name:
        NEW_NAME: Final = file_name.replace(pattern, new_name, 1)
        NEW_PATH: Final = os.path.join(path, NEW_NAME)
        os.rename(file_path, NEW_PATH)


def rename_multiple_files(path: str = '', pattern: str = '', newName: str = '') -> None:
    FILES: Final = get_files_in_folder(path)

    for file in FILES:
        rename_file(file, pattern, newName)


def main(argv: List[str] = []) -> None:
    path = ''
    pattern = ''
    name = ''

    try:
        _, path, pattern, name = argv
    except:
        print('Enter a path to a folder, a pattern and a new file name.')
        exit

    rename_multiple_files(path, pattern, name)


if __name__ == '__main__':
    main(sys.argv)
