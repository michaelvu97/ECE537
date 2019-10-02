import random
import math
import matplotlib.pyplot as plot

N = 100


for rho in [-1, -0.5, 0, 0.5, 1]:
    samples_X = []
    samples_Y = []
    for i in range(N):
        Z1 = random.gauss(0, 1)
        Z2 = random.gauss(0, 1)

        X = 1 + math.sqrt(2) * Z1
        Y = (rho * Z1 + math.sqrt(1 - rho ** 2) * Z2) + 2
        samples_X.append(X)
        samples_Y.append(Y)
    plot.plot(samples_X, samples_Y, 'o')
    plot.show()