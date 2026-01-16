"""
Edited by Yun-An
Date: 2026-Jan-16

Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

# initialization
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
from compute_sta import compute_sta
from compute_sta_all import compute_sta_all


# load data
FILENAME = os.path.join(os.path.dirname(__file__), 'c1p8_3.4.pickle')

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

print("Number of features (keys):", len(data))
print("Feature names:", list(data.keys()))

stim = data['stim']
rho = data['rho']

print(stim.shape)
print(rho.shape)


# Fill in these values
sampling_period = 2  # in ms
num_timesteps = 150  # we want to calculate the 300ms before spikes.
group_size = 50 # we want to see a small group average of sta

# sta calculation
sta = compute_sta(stim, rho, num_timesteps)
sta_all = compute_sta_all(stim, rho, num_timesteps, group_size)


time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

# visualization
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.subplot(2, 1, 2)
plt.plot(time, sta_all)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Individual Spike-Triggered Stimuli')

plt.tight_layout()
plt.show()