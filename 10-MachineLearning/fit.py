import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("fake_regression.txt")
training = data[:][:75]
test = data[:][75:]
x1, y1 = training.T
x2, y2 = test.T

residuals1 = np.zeros(20)
residuals2 = np.zeros(20)
n = np.arange(1, 21)
for i in range(20):
    coeffs = np.polyfit(x1, y1, i+1)
    y_obtained = np.poly1d(coeffs)(x1)
    residuals1[i] = np.sum((y1-y_obtained)**2)/y1.shape
    y_obtained = np.poly1d(coeffs)(x2)
    residuals2[i] = np.sum((y2-y_obtained)**2)/y2.shape

#plt.plot(n, residuals1, "-o", label="Train")
#plt.plot(n, residuals2, "-o", label="Test")
plt.plot(n, abs(residuals1-residuals2), "-o")
#splt.legend()
plt.show()
