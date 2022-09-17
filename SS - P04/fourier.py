import numpy as np
from scipy.integrate import quad
from matplotlib import pyplot as plt

###################################################### PART 1
def fourier(x, t, step, dcp):
    X = np.zeros(len(t))

    for w in range (len(X)):
        def real_part(t):
            return np.real(x(t) * (np.e ** (-1j * (w * step - 15) * t)))
        X[w] = quad(real_part,  -500,  500, limit=5000, points=dcp)[0]

    return X

###################################################### PART 2
step = 0.1 # it took forever for my laptop to give a result when I set it to 0.01...
t = np.linspace(-15, 15, int(30 / step))

f, sp = plt.subplots(2, 2)

#-------------------------------------------

x = lambda t: np.where(abs(t/2) <= 1, 1, 0)
sp[0, 0].plot(t, x(t), label='x1(t)')
res = fourier(x, t, step, [-2, 2])
sp[0, 0].plot(t, res, label='X1(ω)')
sp[0, 0].legend()

#-------------------------------------------

x = lambda t: np.sin(t) / (np.pi * t)
sp[0, 1].plot(t, x(t), label='x2(t)')
res = fourier(x, t, step, [0])
sp[0, 1].plot(t, res, label='X2(ω)')
sp[0, 1].legend()

#-------------------------------------------

x = lambda t: np.cos(t) * np.sin(3 * t) / (np.pi * t)
sp[1, 0].plot(t, x(t), label='x3(t)')
res = fourier(x, t, step, [0])
sp[1, 0].plot(t, res, label='X3(ω)')
sp[1, 0].legend()

#-------------------------------------------

x = lambda t: (np.sin(t) / (np.pi * t)) ** 2
sp[1, 1].plot(t, x(t), label='x4(t)')
res = fourier(x, t, step, [0])
sp[1, 1].plot(t, res, label='X4(ω)')
sp[1, 1].legend()

#-------------------------------------------

plt.show()
