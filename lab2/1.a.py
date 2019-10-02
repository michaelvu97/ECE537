import random
import matplotlib.pyplot as plot

N = 100

samples_X1 = []
samples_X2 = []

for i in range(N):
    samples_X1.append(random.gauss(0, 1))
    samples_X2.append(random.gauss(0, 1))

plot.plot(samples_X1, samples_X2, 'o')
plot.show()
