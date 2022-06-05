'''
Author: Cayas, Von Vic
Date: Sunday, June 5 2022
Description: Functions used for file operations to insert/read card data in files
             in the `shuffles` folder.
'''
import os

def clear():
    '''Deletes all the files in the `shuffles` folder.'''
    shuffle_dir = f'{os.getcwd()}/shuffles'

    remove = lambda f: os.remove(f'{shuffle_dir}/{f}')
    [remove(file) for file in os.listdir(shuffle_dir)]

def insert(file: str, data: list):
    '''Inserts `data` into a file called `file`.'''
    pass

def read(file: str) -> list:
    '''Reads data from `file` and returns it'''
    pass