import numpy as np
import matplotlib.pyplot as plt

def initial(x):
    U = np.zeros_like(x)
    pos = np.intersect1d(np.where(x >= 50), np.where(x < 110))
    U[pos] = 100*np.sin(np.pi*(x[pos]-50)/60)    
    return U
    
dx = 0.1
a = -3.0
dt = 0.015
t_max = 0.45
x = np.arange(0, 300+dx, dx)
N = len(x)
init = initial(x)
plt.plot(x, init)

def fdfd(init, a, t_max, dx, dt):
    t = 0
    U = init.copy()
    c = 0.5*a*dt/dx
    while t <= t_max:
        for i in range(1, N-1):
            U[i] += -c*(U[i+1] - U[i-1])
        t += dt
    return U

init = fdfd(init, a, t_max, dx, dt)
plt.plot(x, init)
plt.show()