import numpy as np
import matplotlib.pyplot as plt

x, y = np.genfromtxt("data.dat").T

plt.plot(x, y, "-D", ms=2)
plt.xlabel('Value')
plt.ylabel('Precision')
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.savefig("plot.pdf")
