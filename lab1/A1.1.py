import random
import matplotlib.pyplot as plot

N = 100

true_expected_mean = 1.25
true_expected_variance = 37.0/48 

def probably():
    p = random.random() # in [0,1)
    if p <= 0.5:
        return random.uniform(0, 1)
    else:
        return random.uniform(1,3)

results = []

for i in range(N):
    results.append(probably())

plot.hist(results)

plot.show()

av = sum(results) / N

variance = sum(map(lambda x: ((x - av)**2), results)) / N;

print("average: {} ({} from true), variance: {} ({} from true)".format(av, av - true_expected_mean, variance, variance - true_expected_variance))

