import matplotlib.pyplot as plt
import numpy as np


def plotuj(time, signal):
    plt.figure(1)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.plot(time, signal)

#svaki segmentic je niz od 120 delica (to je ukupno 25ms na 48khz)
def separate(niz, x, n):
    a = n // x
    res = np.zeros([a * 2 - 1, x])
    brojac = 0
    for i, _ in enumerate(res):
        for j in range(x): 
            res[i][j] = niz[i * (x // 2) + j]
    return res
