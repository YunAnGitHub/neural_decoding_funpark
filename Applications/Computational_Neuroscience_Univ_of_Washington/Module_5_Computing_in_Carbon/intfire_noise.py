"""
Edit by Yun-An Huang
Date: 2026-Feb-09

1. Based on the integrate-and-fire neuron model,
calculate the spike intervals.

2. Change the noise amplitude and plot the histogram.
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

# Initialization
DIR = os.path.dirname(__file__)

# Input current
I = 1 # nA

# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method


tstop = 2000
abs_ref = 5 # Absolute refractory period 
ref = 0 # Absolute refractory period counter

V_th = 10 # Spike threshold


# input current

for noiseamp in range(0,5,1):
    V = 0
    V_trace = []  # Voltage trace for plotting
    spiketimes = [] # List of spike times

    I += noiseamp*np.random.normal(0, 1, (tstop,)) # nA; Gaussian noise

    for t in range(tstop):
    
        if not ref:
            V = V - (V/(R*C)) + (I[t]/C)
        else:
            ref -= 1
            V = 0.2 * V_th # reset voltage
        
        if V > V_th:
            V = 50 # emit spike
            ref = abs_ref # set refractory counter
            spiketimes += [t]

        V_trace += [V]

    # plot V
    plt.figure(figsize=(20, 4))
    plt.plot(V_trace)
    plt.savefig(os.path.join(DIR, f'V_noise_{noiseamp:.2f}.png'))
    plt.close()

    # Plot histogram
    plt.hist(np.diff(spiketimes))
    plt.savefig(os.path.join(DIR, f'Spikes_time_noise_{noiseamp:.2f}.png'))
    plt.close()


    
