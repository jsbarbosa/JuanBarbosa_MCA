import numpy as np
import matplotlib.pyplot as plt
import sys

name = sys.argv[1] # args 
data = np.genfromtxt(name)

plt.hist(data, bins = 50, normed = True) # added bings and normed
plt.savefig("output.pdf")
