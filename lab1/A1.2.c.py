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

pmf = {}

for i in range(N):
    X = probably()
    Y = probably()

    Z1 = X + Y
    Z2 = X - Y
    key = (Z1, Z2)

    if not (key in pmf):
        pmf[key] = 0

    pmf[key] += 1

print(pmf)
