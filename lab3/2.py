import numpy as np
import random
import matplotlib.pyplot as plot

def SampleExp(rate):
    u = random.random()
    return - np.log(u / rate) / rate

def N(t, rate, sample_limit):
    count = 0
    i = 1
    X_sample_sum = 0.0
    X_sample_hist = []
    for i in range(sample_limit):
        X_sample_sum += SampleExp(rate)
        X_sample_hist.append(min(X_sample_sum, t))
        if X_sample_sum < t:
            count += 1

    return count, X_sample_hist

samples_a = [N(5, 2, 20)[1] for n in range(5)]

for sample in samples_a:
    plot.plot(sample)

plot.show()

samples_b = [N(5, 2, 20)[0] for n in range(1000)]

plot.hist(samples_b)
plot.show()