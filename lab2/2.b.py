import random
import math
import matplotlib.pyplot as plot

samples = []

N = 1000

def sample(n):
    total = 0
    for i in range(n):
        total += random.random()
    return total

def Z():
    return (sample(100) - 50) / math.sqrt(100/12)

for n in range(N):
    samples.append(Z())

plot.hist(samples)
plot.show()