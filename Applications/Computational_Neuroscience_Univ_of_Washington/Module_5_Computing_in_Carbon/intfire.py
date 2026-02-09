
"""
Edited by Yun-An Huang
Date: 2026-Feb-09

Based on the integrate-and-fire neuron model,
find the minimum I that can fire the neuron.


"""


from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# initialize
DIR = os.path.dirname(__file__)
I_ini = 0.01
I_step = 0.01
I_max = 1

# input current

#I = 1 # nA
# I = 0.26 # nA

# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

tstop = 200 # ms
abs_ref = 5 # absolute refractory period 
V_th = 10 # spike threshold

for i in np.arange(I_ini, I_max, I_step):
    I = i
    V = 0
    ref = 0 # absolute refractory period counter
    V_trace = []  # voltage trace for plotting
    fired = False
    
    for t in range(tstop):
    
        if not ref:
            V = V - (V/(R*C)) + (I/C)
        else:
            ref -= 1
            V = 0.2 * V_th # reset voltage
        
        if V > V_th:
            V = 50 # emit spike
            ref = abs_ref # set refractory counter
            fired = True
            
        V_trace += [V]
       


    plt.plot(V_trace)
    #plt.show()
    plt.savefig(os.path.join(DIR, f'I_{i:.2f}.png'))
    plt.close()
    
    if fired:
        print(f'Minimum input current to fire: {I:.2f} nA')
        break
