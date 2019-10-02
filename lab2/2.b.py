import random
import math
import matplotlib.pyplot as plot
import numpy as np

samples = []

N = 1000

def sample(n):
    total = 0
    for i in range(n):
        total += random.random()
    return total

def Z():
    # Will adjust the sample to become zero-mean and unit variance.
    return (sample(100) - 50) / math.sqrt(100/12)

for n in range(N):
    samples.append(Z())

def N_pdf(x):
    variance = 1
    mean = 0

    return (1/ math.sqrt(2 * math.pi * variance)) * math.exp((-((x - mean) **2))  / (2 * variance));

# generate a gaussian pdf
gaussian_x = np.linspace(-4, 4, 1000)
gaussian_y = [N_pdf(x) for x in gaussian_x]

fig,ax1 = plot.subplots()

ax1.hist(samples, bins=20)

ax2 = ax1.twinx()
ax2.plot(gaussian_x, gaussian_y, color='red')
plot.show()