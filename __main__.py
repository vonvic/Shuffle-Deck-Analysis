from functools import reduce
from math import sqrt
from random import random
import data

def e_distance(A: list):
    return reduce(lambda p, x: p+sqrt(pow(x-A.index(x), 2)), A)

def shuffle(A: list):
    mid = len(A)//2
    fst, snd = A[:mid], A[mid:]
    
    new_list = []
    for i in range(len(A)):
        value = random()
        
        chosen: int
        if value < 0.5:
            chosen = fst.pop(0) if fst else snd.pop(0)
        else:
            chosen = snd.pop(0) if snd else fst.pop(0)
        new_list.append(chosen)
        
    return new_list

def print_sorted_measurement(A: list):
    sorted_measure = e_distance(A)
    print(sorted_measure)

def A():
    sorted_deck = [i for i in range(52)]
    deck = sorted_deck[:]
    
    shuffle_count = 100
    
    num_of_repeats = 1000
    averages = [0 for _ in range(shuffle_count)]
    for _ in range(num_of_repeats):
        for i in range(shuffle_count):
            deck = shuffle(deck)
            sorted_measure = e_distance(deck)
            averages[i] += sorted_measure
        deck = sorted_deck[:]
    
    averages = list(map(lambda x: x/num_of_repeats, averages))
    for x in averages: print(x)

def main():
    choice = input('Generate new datasets (y/n): ').lower()
    if choice == 'y':
        data.clear()
        # TODO (von-vic): Generate new datasets and store them into a folder called
        # `shuffles`
        pass
    else:
        # TODO (von-vic): Read from the `shuffles` folder.
        pass

if __name__ == '__main__':
    main()