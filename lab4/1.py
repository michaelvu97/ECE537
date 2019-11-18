import matplotlib.pyplot as plt
import numpy as np

def GetN():
    return np.random.normal(0, 1, 600)

def GetX(N):
    X = [0.0] * len(N)
    X[0] = N[0]
    X[1] = N[1] + 1.5 * X[0]
    for i in range(len(N) - 2):
        X[i + 2] = N[i + 2] + 1.5 * X[i + 1] - 0.8 * X[i]

    return X

N = GetN()
X = GetX(N)

# Part A
X = X[:-512]
N = N[:-512]
fig, axs = plt.subplots(2)
x_plot = axs[0].plot(X)
n_plot = axs[1].plot(N)
axs[0].set_ylabel("X")
axs[1].set_ylabel("N")
axs[1].set_xlabel("t")
plt.show()

# Part B
def correlation(a, b, tau):
    return a[tau:] * b[:-tau]

# This part doesn't make a whole lot of sense but
autocorrelation_N = correlation(N, N, 50)
autocorrelation_X = correlation(X, N, 50)
fig, axs = plt.subplots(2)
x_plot = axs[0].plot(autocorrelation_X)
n_plot = axs[1].plot(autocorrelation_N)
axs[0].set_ylabel("X(t)*X(t+50)")
axs[1].set_ylabel("N(t)*N(t+50)")
axs[1].set_xlabel("t")
plt.show()
