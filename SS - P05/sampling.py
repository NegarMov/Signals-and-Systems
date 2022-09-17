import numpy as np
from matplotlib import pyplot as plt

###################################################### PART 1 - a
def sample(x, step, rate):
    interval = int (1 / (rate * step))
    xp = np.zeros(round(len(x) * step * rate))
    for i in range (len(xp)):
        xp[i] = x[i * interval]
    return xp

###################################################### PART 1 - b
step = 0.00001
t = np.linspace(-1, 1, int(2 / step))

x = np.cos(10 * np.pi * t)
plt.plot(t, x, label='Original Signal')

rate = 4
xp = sample(x, step, rate)
plt.plot(np.linspace(-1, 1 - (1 / rate), len(xp)), xp, label='Sampled Signal')

plt.legend()
plt.show()

###################################################### PART 2
x = np.cos(30 * np.pi * t)
plt.plot(t, x, label='Original Signal')

for rate in [20, 30, 40]:
    xp = sample(x, step, rate)
    plt.plot(np.linspace(-1, 1 - (1 / rate), len(xp)), xp, label=f'Sampled Signal ({rate})')

plt.legend()
plt.show()