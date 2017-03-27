#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:21:00 2017

@author: juan
"""

import numpy as np
import matplotlib.pyplot as plt

obs = np.array([1.5, 1.7, 2])
def rand():
    return 2*np.random.random() - 1    

def integral(a, b, lm):
    return -lm*(func(b, lm) - func(a, lm))
    
def func(x, lm):
    return np.exp(-x/lm)
    
def probability(x, lm):
    p = 1
    z = integral(1, 20, lm)
    for x_ in x:
        p *= func(x_, lm)/z
    return p

def bayesian(x, lm):
    return probability(x, lm)

def hastings(N, dx = 1):
    lambdas = np.ones(N+1)
    lambdas[0] = np.random.random()*10.0
    for i in range(N):
        second = lambdas[i] + dx*rand()
        q = bayesian(obs, second)/bayesian(obs, lambdas[i])
        alpha = min(q, 1.0)
        u = np.random.random()
        if u <= alpha and second > 0:
            lambdas[i+1] = second
        else:
            lambdas[i+1] = lambdas[i]
    return lambdas

def rubin(N, M, dl):
    avs = np.zeros(M)
    vas = np.zeros(M)
    
    R = np.zeros(N-2)

    chains = np.array([hastings(N, dl) for i in range(M)])
    for j in range(2, N):
        for i in range(M):
            avs[i] = np.mean(chains[i, :j])
            vas[i] = np.std(chains[i, :j])**2
               
        total = np.mean(avs)
        B = j/(M-1)*np.sum((avs-total)**2)
        W = vas.mean()
        
        R[j-2] = (j-1)/j + (B/W)*(M+1)/(j*M)
    return R

N = 10000
lm = np.logspace(-3, 3, 5)
for l in lm:
    R = rubin(N, 5, l)
    plt.plot(R, label="%f"%l)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
#lam = np.linspace(0.01, 20, 1000)
#dp = lam[1] - lam[0]
#p = bayesian(obs, lam)
#plt.plot(lam, p/(dp*np.trapz(p)))
#plt.hist(lambdas, normed = True, bins = 50, edgecolor="k")
#plt.show()