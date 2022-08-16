import numpy as np
import math

def kvadriraj(signal):
    return np.power(signal, 2)


def active(segment, activity):
    silence = 17 * 1e9
    segment = kvadriraj(segment)
    zbir = sum(segment)
    zbir += zbir * sum(activity) // 2

    if(zbir > silence): return True
    return False


def log_spectrum(magnituda):
    return math.log10(kvadriraj(magnituda) + math.e)
