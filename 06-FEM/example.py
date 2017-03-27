#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:35:55 2017

@author: juan
"""

import numpy as np
import matplotlib.pyplot as plt

def integral(l, m):
    return 1.0/(m+l+1)

def function(x):
    return np.exp(-x)*x**(1/3)

B = np.array([0.218296, 0.141478, 0.103715])

A = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        A[i, j] = integral(i+1, j+1)
        
sol = np.linalg.solve(A.T, B)

x = np.linspace(0, 1, 100)
y = function(x)

y2 = sol[0]*x + sol[1]*x**2 + sol[2]*x**3
plt.plot(x, y)
plt.plot(x, y2)
plt.show()