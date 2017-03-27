#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:29:13 2017

@author: juan
"""

import numpy as np
import matplotlib.pyplot as plt

def U_vector(rho, u, p, v, w, E):
    return rho, rho*u, rho*v, rho*w, rho*E

def F_x(rho, u, p, v, w, E):
    return rho*u, rho*u**2 + p, rho*u*v, rho*u*w, rho*(E+p/rho)*u

def F_y(rho, u, p, v, w, E):
    return rho*v, rho*u*v, rho*v**2 + p, rho*v*w, rho*(E+p/rho)*v

def F_z(rho, u, p, v, w, E):
    return rho*w, rho*u*w, rho*v*w, rho*w**2 + p, rho*(E+p/rho)*w

def splitter(U):
    rho = U[0]
    u = U[1]/rho
    v = U[2]/rho
    w = U[3]/rho
    E = U[4]/rho
    e = E-0.5*(u**2 + v**2+w**2)
    P = rho*e*(gamma-1)
    h = E + P/rho
    c = np.sqrt((gamma+1)*h)
    return rho, u, p, v, w, E

e0 = 1e13 #J/kg
rho0 = 1.0 #kg/m3
u0 = 0.0 #m/s
p0 = 10e5 #atm
gamma = 1.4 #