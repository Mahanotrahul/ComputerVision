import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
from math import radians


f = plt.imread('H:\Vasitars.com\Logo\logo.png')
plt.imshow(f)

def main():
    plt.interactive(False)
    #x = np.arange(0, radians(1800), radians(12))
    #plt.plot(x, np.cos(x), 'b')
    x = range(6)
    #x = np.arange(1,5)
    plt.plot(x , [xi/3 for xi in x], label='Fast')
    plt.plot([0,1,5,10], label='Normal')
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Plot')
    plt.legend()
    plt.show();
    M = np.array([[1,2,3],[4,5,6]])
    print(M[1,0])
    print(range(6))
    print(np.arange(6))
    plt.savefig('plot.png')

    plt.interactive(False)
    
    y = np.random.randn(1000)
    plt.hist(y)
    plt.show()



def interactivewindow():
    import matplotlib as mpl
    mpl.use('GTKAgg')   # to use GTK UI
    plt.plot([1,2,3,4])
    plt.show()



