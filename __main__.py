'''
Author: Cayas, Von Vic
Date: Sunday, June 5 2022
Description: A program to generate and analyze the effect of riffle shuffling a
    standard 52 deck of cards. After obtaining data (whether stored previously
    or generated at runtime), two plots will be made:
        - shows the average euclidean distances
        - shows the differences between two average eucilidean distances
'''
import data
import deck
import graph

AVG_FILE_NAME = 'averages.txt'

def request_int(msg: str) -> int:
    '''Requests a number from the user with a default value'''
    default = 100
    num = input(f"{msg} (default: {default}): ")
    if not num: # default
        num = default
    elif not num.isdigit():
        raise ValueError(f'{num} is not a number.')
    else:
        num = int(num)
    
    return num

def request_shuffle_count() -> int:
    return request_int('Shuffle count')

def request_test_repeat_count() -> int:
    return request_int('Test repeat count')

def delta(A: list):
    return [abs(A[i]-A[i+1]) for i in range(len(A)-1)]

def main():
    choice = input('Generate new datasets (y/n): ').lower()
    averages: list
    if choice == 'y' or choice == 'yes':
        # ======================================================================
        # Request parameters
        # ======================================================================
        shuffle_count = request_shuffle_count()
        repeat_count = request_test_repeat_count()

        averages = deck.generate_averages(shuffle_count, repeat_count)
        data.insert(AVG_FILE_NAME, averages)
    elif choice == 'n' or choice == 'no':
        averages = data.read(AVG_FILE_NAME)
    else:
        raise ValueError(f'{choice} is not a valid choice')

    title = 'Measure of the Effect of Number of Riffle Shuffles on Randomizing A Deck'
    graph.plot(averages, title, 'Shuffle Count', 'Average of sortedness (lower is more sorted)')
    graph.plot(delta(averages), title, 'Shuffle Count', 'Absolute change of deck sortnedness')

    input('Press ENTER to exit')

if __name__ == '__main__':
    main()