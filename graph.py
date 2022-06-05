import matplotlib.pyplot as plt
import numpy as np

_count = 0

def get_count():
    global _count
    _count += 1
    return _count

def plot(A: list, title: str = '', xlabel: str = '', ylabel: str = ''):
    '''Plots a graph from the given parameters, where A is the y values and the
    x values is just the numbers 1 to length of A.'''
    print('Plotting averages...')

    x = np.array([(i+1) for i in range(len(A))])
    y = np.array(A)

    plt.figure(get_count())
    plt.scatter(x, y, s=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()

    plt.ion()
    plt.show()