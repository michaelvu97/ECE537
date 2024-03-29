import random
import matplotlib.pyplot as plot

true_expected_mean = 1.25
true_expected_variance = 37.0/48 

def run(N, showPlot):
    def probably():
        p = random.random() # in [0,1)
        if p <= 0.5:
            return random.uniform(0, 1)
        else:
            return random.uniform(1,3)

    results = []

    for i in range(N):
        results.append(probably())

    if showPlot:
        plot.hist(results)
        plot.show()

    av = sum(results) / N

    variance = sum(map(lambda x: ((x - av)**2), results)) / N;
    return av, variance;


# Part a-c
av, variance = run(100, True)

print("average: {} ({} from true), variance: {} ({} from true)".format(av, av - true_expected_mean, variance, variance - true_expected_variance))

# part d
Ns = [100, 200, 300, 400, 500, 1000, 2000, 5000]

averages = []
variances = []

for n in Ns:
    curr_av, curr_variance = run(n, False)
    averages.append(curr_av)
    variances.append(curr_variance)

plot.plot(Ns, averages)
plot.show()

plot.plot(Ns, variances)
plot.show()