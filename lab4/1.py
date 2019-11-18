import matplotlib.pyplot as plt
import scipy.signal
import numpy as np
import math

def GetN():
    return np.random.normal(0, 1, size=600)

def GetX(N):
    X = [0.0] * len(N)
    X[0] = N[0]
    X[1] = N[1] + 1.5 * X[0]
    for i in range(len(N) - 2):
        X[i + 2] = N[i + 2] + (1.5 * X[i + 1]) - (0.8 * X[i])

    return np.array(X)

N = GetN()
X = GetX(N)

# Part A
X = X[88:]
N = N[88:]
fig, axs = plt.subplots(2)
x_plot = axs[0].plot(X)
n_plot = axs[1].plot(N)
axs[0].set_ylabel("X")
axs[1].set_ylabel("N")
axs[1].set_xlabel("t")
plt.show()

# Part B
# This part doesn't make a whole lot of sense but
autocorrelation_N = np.correlate(N, N, "same")
autocorrelation_X = np.correlate(X, X, "same")

tau_vals= range(-50, 50)

fig, axs = plt.subplots(2)
x_plot = axs[0].plot(tau_vals, autocorrelation_X[256 - 50: 256 + 50])
n_plot = axs[1].plot(tau_vals, autocorrelation_N[256 - 50: 256 + 50])
axs[0].set_ylabel("R_XX(tau)")
axs[1].set_ylabel("R_NN(tau)")
axs[1].set_xlabel("tau")
plt.show()

# Part C
N_traces = [GetN() for n in range(10)]
X_traces = [GetX(n)[88:] for n in N_traces]
N_traces = [n[88:] for n in N_traces]

def periodogram(signal):
    return scipy.signal.periodogram(signal, fs=2*math.pi)

setted = False
avg_periodogram = None
f = None
for x_trace in X_traces:
    f, x_periodogram = periodogram(x_trace)
    if setted:
        avg_periodogram += x_periodogram
    else:
        setted = True
        avg_periodogram = x_periodogram

plt.plot(f, avg_periodogram / 10.0)
w, h = scipy.signal.freqz(X_traces, N_traces) #????
plt.plot(w, np.square(np.abs(h)))
plt.show()

# THIS IS WRONG, THIS ISN'T THE TRANSFER FUNCTION

plt.show()

# Part D
fft = np.abs(np.fft.fft(correlation(X, X, 0)))
plt.plot(fft)
plt.show()