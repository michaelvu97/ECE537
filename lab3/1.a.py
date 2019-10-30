import numpy as np
import random
import matplotlib.pyplot as plot

p = 0.5
q = 1 - p

def bernoulli(p):
    if (random.random() >= p):
        return 1;
    return -1;

N = 500

N_SAMPLES = 50

samples = []

for sample in range(N_SAMPLES):
    curr_sample = []
    curr = 0
    for n in range(N):
        curr += bernoulli(p)
        curr_sample.append(curr)
    samples.append(curr_sample)
    plot.plot(curr_sample)

plot.show()