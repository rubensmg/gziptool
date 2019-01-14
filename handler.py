#!/usr/bin/python
# -*- coding:utf-8 -*-

from os import system, walk
from os.path import join as path_join, exists as path_exists
from tarfile import open as tar_open

COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_CYAN = '\033[36m'
COLOR_WHITE = '\033[0m'
VERSION = '1.0.0'

def banner():
    system('clear')
    text = f'''
    {COLOR_GREEN}GZIP Compression & Decompression Tool{COLOR_WHITE}\n
    {COLOR_CYAN}Created By: Rubens M. Gomes{COLOR_WHITE}
    {COLOR_CYAN}Version: {VERSION}{COLOR_WHITE}
    '''
    print(text)


def compress():
    print(f'\n{COLOR_GREEN}[*] Directory:{COLOR_WHITE}')
    path = input(f'{COLOR_RED}[>] {COLOR_WHITE}')
    print(f'{COLOR_GREEN}[*] Compressed File Name (Without extension):{COLOR_WHITE}')
    filename = input(f'{COLOR_RED}[>] {COLOR_WHITE}')

    with tar_open(f'{filename}.tar.gz', 'w:gz') as tarball:
        [
            [
                tarball.add(path_join(dirpath, f))
                for f in filenames
            ]
            for dirpath, _, filenames in walk(path)
        ]
        tarball.close()
    print(f'{COLOR_GREEN}File {filename}.tar.gz created{COLOR_WHITE}')


def decompress():
    print(f'\n{COLOR_GREEN}[*] Compressed File Name (Without extension):{COLOR_WHITE}')
    filename = input(f'{COLOR_RED}[>] {COLOR_WHITE}')
    print(f'{COLOR_GREEN}[*] Directory to decompress:{COLOR_WHITE}')
    path = input(f'{COLOR_RED}[>] {COLOR_WHITE}')
    
    with tar_open(f'{filename}.tar.gz') as tarball:
        tarball.extractall(path=path)
        tarball.close()


def core():
    while True:
        print(f'\n{COLOR_GREEN}[*] Actions:{COLOR_WHITE}')
        print(f'{COLOR_GREEN}[1] Compress{COLOR_WHITE}')
        print(f'{COLOR_GREEN}[2] Decompress{COLOR_WHITE}')
        print(f'{COLOR_GREEN}[Ctrl+C] - Exit{COLOR_WHITE}')

        choice = input(f'{COLOR_RED}[>] {COLOR_WHITE}')

        if choice == '1':
            compress()
        elif choice == '2':
            decompress()
        else:
            print(f'{COLOR_RED}[-]Invalid Choice{COLOR_WHITE}\n')
            core()


if __name__ == '__main__':
    try:
        banner()
        core()
    except KeyboardInterrupt:
        print('\nGood Bye!\n')
