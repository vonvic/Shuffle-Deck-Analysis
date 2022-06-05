'''
Author: Cayas, Von Vic
Date: Sunday, June 5 2022
Description: Functions used for file operations to insert/read card data in files
             in the `shuffles` folder.
'''
import os
import sys

def insert(file: str, data: list) -> bool:
    '''Inserts `data` into a file called `file`.'''
    try:
        with open(f'shuffles/{file}', 'w') as f:
            for x in data:
                f.write(f'{x}\n')
        return True
    except Exception as e:
        sys.stderr.write(str(e))
        return False

def read(file: str) -> list:
    '''Reads data from `file` and returns a list of 2-length tuples.'''

    data: list
    with open(f'shuffles/{file}', 'r') as f:
        data = [x[:-1] for x in f.readlines()]
    return data