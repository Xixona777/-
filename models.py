Python

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import constants



m0 = 40660
M = m0 + 3562 * 4 + 3000 + 36000 + 50 + 100 + 175 * 4 + 175
Ft = 3268861.02
Cf = 0.5
ro = 2.293
S = constants.pi * ((6.6 / 2) ** 2)
g = 1.00034 * constants.g
k = (M - m0) / (80 + 5)


def A(t):
    return (Ft / (M - k * t))


def B(t):
    return ((Cf * ro * S) / (2 * (M - k * t)))


def dv_dt(t, v):
    return (A(t) - B(t) * v ** 2 - g)


v0 = 0

t = np.linspace(0, 700, 1080)

solve = integrate.solve_ivp(dv_dt, t_span=(0, max(t)), y0=[v0], t_eval=t)

x = solve.t
y = solve.y[0]

plt.figure(figsize=(7, 6))
plt.plot(x, y, '-r', label="v(t)")
plt.legend()
plt.grid(True)
plt.show()
