#!/usr/bin/python3
import sys
import os
from typing import List


def get_folder_content(path: str = '') -> List[str]:
    return os.listdir(path) if path else []


def get_files_in_folder(path: str = '') -> List[str]:
    folder_content = get_folder_content(path)
    return [os.path.join(path, file) for file in folder_content if os.path.isfile(os.path.join(path, file))]


def rename_file(filePath: str = '', pattern: str = '', newName: str = ''):
    path, fileName = os.path.split(filePath)

    if pattern and pattern in fileName:
        newFileName = fileName.replace(pattern, newName, 1)
        newPath = os.path.join(path, newFileName)
        os.rename(filePath, newPath)


def rename_multiple_files(path, pattern, newName):
    files = get_files_in_folder(path)
    for file in files:
        rename_file(file, pattern, newName)


if __name__ == '__main__':
    path = ''
    pattern = ''
    name = ''

    try:
        path = sys.argv[1]
        pattern = sys.argv[2]
        name = sys.argv[3]
    except:
        print('Enter a path to a folder, a pattern and a new file name')
        exit

    rename_multiple_files(path, pattern, name)