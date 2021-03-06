import numpy as np
import matplotlib.pyplot as plt

def like(q):
	return np.exp(-q**2)

def loglike(q):
	return -q**2

def deriv_loglike(q):
	return -2*q

def H(q, p):
	k = 0.5*p**2
	u = -loglike(q)
	return k + u

def leapfrog(q, p, dt = 1e-3, inter = 5):
	q_new = q
	p_new = p
	for i in range(inter):
		p_half = p_new + 0.5*dt*deriv_loglike(q_new)
		q_new += dt*p_half
		q_new = p_half + 0.5*dt*deriv_loglike(q_new)
	return q_new, -p_new

def chain(steps = 500):
	q = np.zeros(steps)
	p = np.zeros(steps)
	q[0] = np.random.normal()
	for i in range(steps-1):
		p[i] = np.random.normal()
		q_new, p_new = leapfrog(q[i], p[i])
		alpha = np.exp(-H(q_new, p_new)+H(q[i], p[i]))
		alpha = min(1, alpha)
		if alpha > np.random.random():
			q[i+1] = q_new
		else:
			q[i+1] = q[i]
	return q, p

q, p = chain(10000)
plt.hist(q[500:], bins=20, normed=True)
#plt.plot(q, p)
plt.show()


	
