import random
import math
import matplotlib.pyplot as plot

vals = [0]

N = 1000

def sample(n):
    total = 0
    for i in range(n):
        total += random.random()
    return total

for n in range(1, N + 1):
    vals.append(sample(n) / n)

plot.plot(vals)
plot.xlabel("n")
plot.ylabel('Sn / n')
plot.show()