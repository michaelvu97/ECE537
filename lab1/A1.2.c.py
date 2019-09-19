import random
import matplotlib.pyplot as plot

def probably():
    r = random.random()

    if r <= 0.25:
        return 1
    if r <= 0.5:
        return 2
    if r <= 0.5 + 0.125:
        return 3
    if r <= 0.5 + (0.125 * 2):
        return 4
    if r <= 0.5 + (0.125 * 3):
        return 5

    return 6

N = 1000000

pmf_sampled = [[0 for i in range(6)] for j in range(6)]

for i in range(N):
    X = probably()
    Y = probably()
    pmf_sampled[X - 1][Y - 1] += 1

print pmf_sampled

plot.imshow(pmf_sampled)
plot.show()
