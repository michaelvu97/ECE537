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

"""
FX(x)=1-exp(-rate * x)
x=1-exp(-rate * y)
(1-x)=exp(-rate * y)
ln(1-x)=-rate * y
FX(x) = -ln(1-u)/rate
"""

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

poisson_pmf = PoissonPmf(rate, t, 20)
print(poisson_pmf)

fig,ax1 = plot.subplots()
ax1.hist(samples_b)

ax2 = ax1.twinx()
ax2.plot(poisson_pmf, color='red')

# ax1.set_xlabel('Z_100')
# ax1.set_ylabel('Count')
# ax2.set_ylabel('Unit Gaussian PDF')
plot.show()

