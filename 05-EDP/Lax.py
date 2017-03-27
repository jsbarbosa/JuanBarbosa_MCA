import numpy as np
import matplotlib.pyplot as plt

def initial(x):
    U = np.zeros_like(x)
    pos = np.where(x <= 2)
    U[pos] = 1
    return U

dx = 0.05
t = 0.0
dt = dx*0.5
t_max = 0.5
x = np.arange(0, 4+dx, dx)
U = initial(x)
c = 0.5*dt/dx
plt.plot(x, U)
for i in range(5):
    U = initial(x)
    t = 0
    while t < t_max*i:
        F = 0.5*U**2
        U[1:-1] = 0.5*(U[2:]+U[:-2]) - c*(F[2:]-F[:-2])
        t += dt
    plt.plot(x, U, label = "t = %.2f"%t)
plt.legend()
plt.show()