import numpy as np
import matplotlib.pyplot as plt
def generator(xstart,xstop,n):

    val = (xstop-xstart)/(n-1)
    wezly = np.array([xstart])

    for i in range(1,n,1):
        wezly = np.block([wezly, i * val + xstart])

    elementy = np.zeros((n-1,2))

    for i in range(0, n-1, 1):
        elementy[i][0] = i+1
        elementy[i][1] = i+2

    return wezly,elementy

def plot_g(wezly,elementy, n):
    tab=np.zeros((n))
    l1 = plt.plot(wezly,tab)
    for i in range(0,n-1,1):
        plt.text(wezly[i], 0, "|")
        plt.text(wezly[i+1]/2+wezly[i]/2, 0.003 ,str(i+1))
        plt.text(wezly[i], -0.02, str(i+1))

wezly, elementy = generator(0,1,4)
plot_g(wezly, elementy, len(wezly))

