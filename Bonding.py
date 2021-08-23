# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 11:06:58 2016

@author: matthewrowley1
"""

import numpy as np
from matplotlib import pyplot as plt

xvals = np.linspace(-5,8,1000)

def A(x):
    return np.exp(-np.abs(x))
    
    
def B(x):
    return np.exp(-np.abs(x-3))

AO = A(xvals)**2 + B(xvals)**2
AO = AO / np.sum(AO)

bonding = (A(xvals)+B(xvals))**2 / np.sum((A(xvals)+B(xvals))**2)

antibonding = (A(xvals)-B(xvals))**2 / np.sum((A(xvals)-B(xvals))**2)
plt.figure()
plt.plot(xvals, AO, label ='Atomic Orbitals Density', linewidth=2)
plt.plot(xvals, bonding, label ='Bonding', linewidth=2)
plt.plot(xvals, antibonding, label = 'Antibonding', linewidth=2)
plt.fill(xvals, bonding - AO, label = 'Bonding - AO', linewidth = 2, alpha=0.7)
plt.fill(xvals, antibonding - AO, label = 'Antionding - AO', linewidth = 2, alpha=0.7)
plt.legend()
plt.show()