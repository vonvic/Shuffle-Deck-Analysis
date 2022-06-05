'''
Author: Cayas, Von Vic
Date: Sunday, June 5 2022
Description: Functions to generate a list of averages to be used for analysis on
the riffle shuffle..
'''

from random import random
from functools import reduce
from math import sqrt

def _e_distance(A: list):
    '''Returns the summation of the euclidean distance of each number in A, where
    the correct value of x is its index.
    E.g. if i == 4, then A[i] == 4'''
    return reduce(lambda p, x: p+sqrt(pow(x-A.index(x), 2)), A)

def _shuffle(A: list):
    '''Shuffles A in a riffle shuffle, where the deck is split in half, and each
    card inserted is from either half with a 50/50 chance.'''
    mid = len(A)//2
    fst, snd = A[:mid], A[mid:]
    
    new_list = []
    for _ in range(len(A)):
        value = random()
        
        chosen: int
        if value < 0.5:
            chosen = fst.pop(0) if fst else snd.pop(0)
        else:
            chosen = snd.pop(0) if snd else fst.pop(0)
        new_list.append(chosen)
        
    return new_list

def generate_averages(shuffle_count, repeat_count):
    '''Generates a list of averages of the 'sortedness' of a sorted deck after a
    number of shuffles. After each shuffle (upto `shuffle_count`), the
    'sortedness' will be added to to the average list at its corresponding
    location. (e.g. the 6th shuffle will have its sortedness added to
    `averages[6]`.'''

    print("Generating new datasets...")
    
    sorted_deck = [i for i in range(52)]
    deck = sorted_deck[:]

    averages = [0 for _ in range(shuffle_count)]
    for _ in range(repeat_count):
        for shuffle_i in range(shuffle_count):
            deck = _shuffle(deck)
            sorted_measure = _e_distance(deck)
            averages[shuffle_i] += sorted_measure
        deck = sorted_deck[:]
    
    averages = list(map(lambda x: x/repeat_count, averages))
    return averages