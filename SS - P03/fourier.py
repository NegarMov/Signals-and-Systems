import numpy as np
from scipy.integrate import quad
from scipy.signal import square
from matplotlib import pyplot as plt

###################################################### PART 1
def fourier(x, T, c):
    a = np.zeros(c + 1)
    b = np.zeros(c + 1)
    w = 2 * np.pi / T

    for k in range (c + 1):
        a[k] = 2 / T * quad(lambda t: x(t) * np.cos(k * w * t), 0, T)[0]
        b[k] = 2 / T * quad(lambda t: x(t) * np.sin(k * w * t), 0, T)[0]

    return a, b

###################################################### PART 2
def reconstruct(a, b, T, t):
    w = 2 * np.pi / T
    x = np.full(len(t), a[0] / 2)

    for k in range (1, len(a)):
        x += a[k] * np.cos(k * w * t) + b[k] * np.sin(k * w * t)

    return x

###################################################### PART 3
step = 0.01
t = np.linspace(-6, 6, int(12 / step))

T = 6
x = lambda t: square(2 / T * np.pi * t)
plt.plot(t, x(t))

for c in range (11):
    a, b = fourier(x, T, c)
    plt.plot(t, reconstruct(a, b, T, t), label='c = {}'.format(c))

plt.legend()
plt.show()
