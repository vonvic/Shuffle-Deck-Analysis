import data
import deck
import graph

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
        data.insert('averages.txt', averages)
    elif choice == 'n' or choice == 'no':
        averages = data.read('averages.txt')
    else:
        raise ValueError(f'{choice} is not a valid choice')
    print(averages)
    title = 'Measure of the Effect of Number of Riffle Shuffles on Randomizing A Deck'
    graph.plot(averages, title, 'Shuffle Count', 'Average of sortedness (lower is more sorted)')

if __name__ == '__main__':
    main()