import numpy as np
from matplotlib import pyplot as plt

###################################################### PART 1
def convolve(x1, x2):
    res_len = len(x1) + len(x2) - 1
    y = np.zeros(res_len)

    for n in range (res_len):
        for k in range (len(x1)):
            y[n] += x1[k] * x2[n-k] if (n - k >= 0 and n - k < len(x2)) else 0

    return y

###################################################### PART 2
step = 0.01
t = np.linspace(0, 10, int(10 / step))

u1 = np.zeros(t.shape)
u1[int(10/step):] = 1
u2 = np.ones(t.shape)
x1 = u1 - u2
plt.subplot(1, 3, 1)
plt.plot(x1)
plt.title("x1(t)", color='green')

x2 = np.zeros(t.shape)
x2[:int(5/step)] = t[:int(5/step)]
x2[int(5/step):int(10/step)] = 5 - t[int(5/step):int(10/step)]
plt.subplot(1, 3, 2)
plt.plot(x2)
plt.title("x2(t)", color='green')

res = convolve(x1, x2)
plt.subplot(1, 3, 3)
plt.plot(np.linspace(0, len(res) * step, len(res)), res * step)
plt.title("x1(t) * x2(t)", color='green')

plt.show()

###################################################### PART 3
n = np.arange(0, 6, 1)
u1 = np.zeros(n.shape)
u1[5:] = 1
u2 = np.ones(n.shape)
h = (0.9 ** n) * (u1 - u2)
plt.subplot(1, 3, 1)
plt.stem(h)
plt.title("h[n]", color='green')

n = np.arange(0, 11, 1)
u3 = np.ones(n.shape)
u4 = np.zeros(n.shape)
u4[10:] = 1
x = ((1 / 3) ** n) * (u3 - u4)
plt.subplot(1, 3, 2)
plt.stem(x)
plt.title("x[n]", color='green')

plt.subplot(1, 3, 3)
plt.stem(convolve(h, x))
plt.title("y[n]", color='green')

plt.show()