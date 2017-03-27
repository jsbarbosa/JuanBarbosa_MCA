import numpy as np
import matplotlib.pyplot as plt



dx = 0.01
t = 0.0
dt = 0.5*dx
t_max = 1.0
x = np.arange(0, 1+dx, dx)
N = len(x)

gamma = 1.4
rho = np.ones(N)
rho[np.where(x>0.5)] = 0.125
p = np.ones(N)
p[np.where(x>0.5)] = 0.1   
u = np.zeros(N)
e = p/(gamma - 1) + 0.5*rho*u**2
U = np.array([rho, rho*u, e])
print(U)
#F = [u*rho, rho*u**2 + p, u*(e+p)]

delta = dt/dx        
def mac(U):
    U_t = U.copy()
    U_i = U[:, 1:-1]
    U_ii = U[:, 2:]
    U_t[:, 1:-1] = U_i - delta*(F(U_ii) - F(U_i))
    
    U[:, 1:-1] = 0.5*(U_i + U_t[:, 1:-1] - delta*(F(U_t[:, 1:-1]) - F(U_t[:,:-2])))
    return U

def F(U):
    rho_ = U[0]
    u_ = U[1]/rho_
    e_ = U[2]
    p_ = (gamma-1)*(e_-0.5*rho_*u_**2)
    return np.array([u_*rho_, rho_*u_**2 + p_, u_*(e_+p_)])

def iterator(U):
    t = 0
    while t < t_max:
        U = mac(U)
        t += dt
    return U

U = iterator(U)
plt.plot(x, U[1])
plt.show()
#for i in range(5):
#    U = initial(x)
#    t = 0
#    while t < t_max*i:
#        F = 0.5*U**2
#        U[1:-1] = 0.5*(U[2:]+U[:-2]) - c*(F[2:]-F[:-2])
#        t += dt
#    plt.plot(x, U, label = "t = %.2f"%t)
#plt.legend()
#plt.show()