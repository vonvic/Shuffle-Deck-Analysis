'''
Author: Cayas, Von Vic
Date: Sunday, June 5 2022
Description: Functions used for file operations to insert/read card data in files
             in the `shuffles` folder.
'''
import sys

def insert(file: str, data: list) -> bool:
    '''Inserts `data` into a file called `file`.'''
    print(f'Writing to shuffles/{file}')
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

    print(f'Reading from shuffles/{file}')
    data: list
    with open(f'shuffles/{file}', 'r') as f:
        data = [float(x[:-1]) for x in f.readlines()]
    return data