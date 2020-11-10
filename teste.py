import numpy as np
import scipy as sp
import math
from scipy.io.wavfile import read
from scipy.io.wavfile import write     # Imported libaries such as numpy, scipy(read, write), matplotlib.pyplot
from scipy import signal
import matplotlib.pyplot as plt

def main():
    data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
    scaled = np.int16(data/np.max(np.abs(data)) * 32767)
    print(scaled)
    write('test.wav', 44100, scaled)#produz 1 segundo de ruído
    return

if __name__ == "__main__":
    main()