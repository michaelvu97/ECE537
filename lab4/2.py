import numpy as np
import random
import scipy.signal
import matplotlib.pyplot as plt

# Part a
def GetN():
    return np.random.standard_normal(size=600)

def GetS(N):
    S = [0.0] * len(N)
    S[0] = N[0]
    S[1] = N[1] + 0.2 * S[0]
    for i in range(len(N) - 2):
        S[i + 2] = N[i + 2] + (0.2 * S[i + 1]) - (0.8 * S[i])

    return np.array(S)

N = GetN()
S = GetS(N)
W = GetN()

N = N[88:]
S = S[88:]
W = W[88:]

# Part A
X = S + W

# Part B
X_correlations = np.correlate(X, X, mode='same')
plt.plot(range(-256, 256), X_correlations)
plt.show()
# It's an even function because X is real-valued.

# Part C
cross_corr = np.correlate(S, X, mode="same")
plt.plot(range(-256, 256), cross_corr)
plt.show()

# Part D
