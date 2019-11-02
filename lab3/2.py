import numpy as np
import random
import math
import matplotlib.pyplot as plot

def SampleExp(rate):
    u = random.random()
    return - np.log(u) / rate

def PoissonPmf(rate, t, limit):
    result = []
    for k in range(limit):
        result.append(np.exp(-rate * t) * ((rate  * t) ** k) / math.factorial(k))

    return result

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

rate = 2
t = 5
limit = 20

samples_a = [N(t, rate, limit)[1] for n in range(5)]

for sample in samples_a:
    plot.plot(sample)

plot.show()



samples_b = [N(t, rate, limit)[0] for n in range(1000)]

expected_value_N = sum(samples_b)/1000.0
print("Expected value of N(t) for t = 5, rate = 2: " + str(expected_value_N))

variance_value_N = sum([(x - expected_value_N) ** 2 for x in samples_b]) / 1000.0
print("Variance value of N(t) for t = 5, rate = 2: " + str(variance_value_N))

theoretical = t * rate

print("The theoretical expected value is " + str(theoretical))
poisson_pmf = PoissonPmf(rate, t, 20)

fig,ax1 = plot.subplots()
ax1.hist(samples_b)

ax2 = ax1.twinx()
ax2.plot(poisson_pmf, color='red')

plot.show()

