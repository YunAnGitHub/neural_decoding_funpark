"""
Edited by Yun-An Huang
Date: 2026-Feb-17

1. Vary the t_peak and observe the spike counts.

Created on Wed Apr 22 16:13:18 2015

Fire a neuron via alpha function synapse and random input spike train
R Rao 2007

translated to python by rkp 2015
"""
from __future__ import print_function, division

import time
import numpy as np
from numpy import concatenate as cc
import matplotlib.pyplot as plt
import os

# Initialize
DIR = os.path.dirname(__file__)
save_path1 = os.path.join(DIR, 'varying_t_peak')
if not os.path.exists(save_path1):
    os.makedirs(save_path1)

t_peaks = np.arange(0.5,10,0.5)

Spike_Counts_All = []

for t_peak in t_peaks:

    
    np.random.seed(0) # Set the seed

    # I & F implementation dV/dt = - V/RC + I/C
    h = 1. # Step size, Euler method, = dt ms
    t_max= 200 # ms, Simulation time period
    tstop = int(t_max/h) # Number of time steps
    ref = 0 # Refractory period counter

    # Generate random input spikes
    # Note: This is not entirely realistic - no refractory period
    # Also: if you change step size h, input spike train changes too...
    thr = 0.9 # Threshold for random spikes
    spike_train = np.random.rand(tstop) > thr

    # Alpha function synaptic conductance
    t_a = 100 # Max duration of syn conductance
    #t_peak = 1 # ms
    g_peak = 0.05 # nS (peak synaptic conductance)
    const = g_peak / (t_peak*np.exp(-1));
    t_vec = np.arange(0, t_a + h, h)
    alpha_func = const * t_vec * (np.exp(-t_vec/t_peak))
    
    
    plt.figure(1)
    plt.plot(t_vec[:80], alpha_func[:80])
    plt.xlabel('t (in ms)')
    plt.title(f"Alpha Function (Synaptic Conductance for Spike at t=0), t_peak = {t_peak} ms")
    plt.savefig(os.path.join(save_path1, f'alpha_function_t_peak_{t_peak}.png')) 
    plt.close()


    # Capacitance and leak resistance
    C = 0.5 # nF
    R = 40 # M ohms
    print('C = {}'.format(C))
    print('R = {}'.format(R))

    # Conductance and associated parameters to simulate spike rate adaptation
    g_ad = 0
    G_inc = 1/h
    tau_ad = 2

    # Initialize basic parameters
    E_leak = -60 # mV, equilibrium potential
    E_syn = 0 # Excitatory synapse (why is this excitatory?)
    g_syn = 0 # Current synaptic conductance
    V_th = -40 # Spike threshold (mV)
    V_spike = 50 # Spike value (mV)
    ref_max = 4/h # Starting value of refractory period counter
    t_list = np.array([], dtype=int)
    V = E_leak
    V_trace = [V]
    t_trace = [0]
    Spike_Counts = 0

    plt.figure(2)
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(np.arange(0,t_max,h), spike_train)
    axs[0].set_title('Input spike train')

    for t in range(tstop):

        # Compute input
        if spike_train[t]: # Check for input spike
            t_list = cc([t_list, [1]])

        # Calculate synaptic current due to current and past input spikes
        g_syn = np.sum(alpha_func[t_list])
        I_syn = g_syn*(E_syn - V) 

        # Update spike times
        if np.any(t_list):
            t_list = t_list + 1
            if t_list[0] == t_a: # Reached max duration of synaptic conductance
                t_list = t_list[1:]

        # Compute membrane voltage
        # Euler method: V(t+h) = V(t) + h*dV/dt
        if not ref:
            V = V + h*(-((V-E_leak)*(1+R*g_ad)/(R*C)) + (I_syn/C))
            g_ad = g_ad + h*(-g_ad/tau_ad) # spike rate adaptation
            g_ad = g_ad + h*(-g_ad/tau_ad) # Spike rate adaptation
        else:
            ref -= 1
            V = V_th - 10 # Reset voltage after spike

        # Generate spike
        if (V > V_th) and not ref:
            V = V_spike
            ref = ref_max
            g_ad = g_ad + G_inc
            
            # Count the spikes
            Spike_Counts += 1
        

        V_trace += [V]
        t_trace += [t*h]
        
        
    # Plot the spike train
    axs[1].plot(t_trace,V_trace)
    plt.draw()
    axs[1].set_title('Output spike train')
    plt.savefig(os.path.join(save_path1, f'trace_t_peak_{t_peak}.png')) 
    plt.close()

    Spike_Counts_All.append(Spike_Counts)

# Plot the changes of t_peaks vs spike counts
plt.plot(t_peaks, Spike_Counts_All) 
plt.xlabel('t_peaks (in ms)')
plt.title(f"Spikes Count vs t_peak")
plt.savefig(os.path.join(DIR, f't_peak_spikes_count.png'))
plt.close()
