from matplotlib import pyplot as plt
from scipy import signal
import numpy as np
import math 

step = 0.01

x = np.linspace(-1 * math.pi, math.pi, int(2 * math.pi / step))
y = np.sin(x)
plt.subplot(2, 3, 1)
plt.title('(a)', color='red')
plt.plot(x, y)

x = np.arange(-5, 6, 1)
y = np.zeros(len(x))
for i in range(len(x)):
    if (x[i] < 0):
        y[i] = -1 * x[i] - 1
    else:
        y[i] = x[i] ** 2
plt.subplot(2, 3, 2)
plt.title('(b)', color='red')
plt.stem(x, y)

x = np.arange(-5, 11, 1)
u = np.zeros(x.shape)
u[3:] = 1
y = (math.e ** (3 * x)) * u + 2 * signal.unit_impulse(len(x), 5)
plt.subplot(2, 3, 3)
plt.title('(c)', color='red')
plt.stem(x, y)

x = np.linspace(-5, 5, int(10 / step))
u1 = np.zeros(x.shape)
u1[int(7/step):] = 1
u2 = np.zeros(x.shape)
u2[int(3/step):] = 1
y = u1 - u2
plt.subplot(2, 3, 4)
plt.title('(d)', color='red')
plt.plot(x, y)

x = np.arange(-10, 11, 1)
y = np.cos(x * 3)
plt.subplot(2, 3, 5)
plt.title('(e)', color='red')
plt.stem(x, y)

x = np.arange(-10, 11, 1)
y = np.cos(x * 3 * math.pi)
plt.subplot(2, 3, 6)
plt.title('(f)', color='red')
plt.stem(x, y)

plt.show()