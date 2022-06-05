'''
Author: Cayas, Von Vic
Date: Sunday, June 5 2022
Description: Functions used for file operations to insert/read card data in files
             in the `shuffles` folder.
'''
import os
import sys

def clear():
    '''Deletes all the files in the `shuffles` folder.'''
    shuffle_dir = 'shuffles'

    remove = lambda f: os.remove(f'{shuffle_dir}/{f}')
    [remove(file) for file in os.listdir(shuffle_dir)]

def insert(file: str, data: list) -> bool:
    '''Inserts `data` into a file called `file`.'''
    try:
        with open(f'shuffles/{file}', 'w') as f:
            for card, sortedness in data:
                f.write(f'{card},{sortedness}\n')
        return True
    except Exception as e:
        sys.stderr.write(e)
        return False

def read(file: str) -> list:
    '''Reads data from `file` and returns it'''
    pass