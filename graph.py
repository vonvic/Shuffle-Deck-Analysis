import matplotlib.pyplot as plt
import numpy as np

def _logFit(x,y):
    # cache some frequently reused terms
    sumy = np.sum(y)
    sumlogx = np.sum(np.log(x))

    b = (x.size*np.sum(y*np.log(x)) - sumy*sumlogx)/(x.size*np.sum(np.log(x)**2) - sumlogx**2)
    a = (sumy - b*sumlogx)/x.size

    return a,b

def plot(A: list, title: str = '', xlabel: str = '', ylabel: str = ''):
    x = np.array([(i+1) for i in range(len(A))])
    y = np.array(A)

    plt.scatter(x, y, s=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()