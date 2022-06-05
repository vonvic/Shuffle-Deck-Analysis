import matplotlib.pyplot as plt
import numpy as np

def plot(A: list, title: str = '', xlabel: str = '', ylabel: str = ''):
    x = np.array([(i+1) for i in range(len(A))])
    y = np.array(A)

    plt.scatter(x, y, s=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()