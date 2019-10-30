import numpy as np
import random
import matplotlib.pyplot as plot

p = 0.5

def bernoulli(p):
    if (random.random() >= p):
        return 1;
    return -1;

N = 500

N_SAMPLES = 50

# 1.a
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

# 1.b
expected_value_n = []
for n in range(N):
    curr = 0.0
    for sample in range(N_SAMPLES):
        curr += samples[sample][n]
    curr /= N_SAMPLES
    expected_value_n.append(curr)

plot.plot(expected_value_n)
plot.show()

# 1.c
variances_n = []
for n in range(N):
    var = 0.0
    mean = expected_value_n[n]
    for sample in range(N_SAMPLES):
        var += (samples[sample][n] - mean) ** 2
    var /= N_SAMPLES
    variances_n.append(var)

plot.plot(variances_n)
plot.show()

# 1.d
samples = []
p = 0.6
for sample in range(N_SAMPLES):
    curr_sample = []
    curr = 0
    for n in range(N):
        curr += bernoulli(p)
        curr_sample.append(curr)
    samples.append(curr_sample)
    plot.plot(curr_sample)

plot.show()

# 1.e
samples = []
p = 0.4
for sample in range(N_SAMPLES):
    curr_sample = []
    curr = 0
    for n in range(N):
        curr += bernoulli(p)
        curr_sample.append(curr)
    samples.append(curr_sample)
    plot.plot(curr_sample)

plot.show()