import random
import math
import matplotlib.pyplot as plot

N = 100


rho = 0.5
samples_X = []
samples_Y = []
for i in range(N):
    Z1 = random.gauss(0, 1)
    Z2 = random.gauss(0, 1)

    X = 1 + math.sqrt(2) * Z1
    Y = (rho * Z1 + math.sqrt(1 - rho ** 2) * Z2) + 2
    samples_X.append(X)
    samples_Y.append(Y)
plot.hist(samples_X)
plot.xlabel('X1')
plot.ylabel('Count')
plot.show()

mean = sum(samples_X)/len(samples_X)
var = sum((float(x) - mean)**2 for x in samples_X) / len(samples_X)

print("mean: " + str(mean))
print("\nvar: " + str(var))