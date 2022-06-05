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

    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

    # def logFunc(x, a, b):
    #     print(x, a, b)
    #     return a + b*np.log(x)

    # plt.plot(x, y, ls="none", marker='.')

    # xfit = np.linspace(0,2000,num=200)
    # plt.plot(xfit, logFunc(xfit, *_logFit(x,y)))

    # z = np.polyfit(x, np.log(y), 2)
    # p = np.poly1d(z)
    
    # plt.plot(x, p(x))
    # plt.show()