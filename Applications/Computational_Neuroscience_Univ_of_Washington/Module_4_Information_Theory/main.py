# This script is to study
#  1. the tuning curve of 4 simulated neurons
#  2. predict the stimuli by using population vector
#
# Date: 2026-Feb-3
# Author: Yun-An Huang


# Initialization

import pickle
import os
import numpy as np
import matplotlib.pyplot as plt


#### Study 1 ####

Neuron_Num = 4 # 4 simulated neurons

# Load data
FILENAME = os.path.join(os.path.dirname(__file__), 'tuning_3.4.pickle')
with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

# There are 5 keys: 'stim', 'neuron1', 'neuron2', 'neuron3', 'neuron4'
# 'stim' stores the stimulus angles
# 'neuronX' stores the firing rate of each neuron

print(data.keys())
print(data['stim'])
print(data['stim'].shape)    # There are 24 stimulus angles
print(data['neuron1'].shape) # Each neuron has 24 angles, and 100 trials.

# Calculate the mean firing rate (tuning curve) of each neuron

mean_tuning_curve = np.zeros((4,data['stim'].shape[0]))

for i in range(Neuron_Num):
    mean_tuning_curve[i] = np.mean(data[f'neuron{i+1}'],axis=0, keepdims=True)

print(mean_tuning_curve.shape)

# Plot the tuning curve
plt.figure(figsize=(10, 8))

for i in range(Neuron_Num):
    plt.subplot(2, 2, i+1)  
    plt.plot(data['stim'], mean_tuning_curve[i])
    plt.xlabel('Stim')
    plt.ylabel('Firing rate (Hz)')
    plt.title(f'Tuning curve of neuron {i+1}')

plt.tight_layout()
plt.draw()
plt.savefig(os.path.join(os.path.dirname(__file__), 'neuron_tuning.png'))
plt.close() # Close the figure internally so memory doesn't explode

# Find the peak firing rate of each neuron
peak_firing_rate = np.zeros((Neuron_Num,))
peak_firing_index = np.zeros((Neuron_Num,))

for i in range(Neuron_Num):
    peak_firing_rate[i] = np.max(mean_tuning_curve[i])
    peak_firing_index[i] = np.argmax(mean_tuning_curve[i])
    print(f'Neuron {i+1} peak firing rate: {peak_firing_rate[i]}')
    print(f'Neuron {i+1} peak firing angle: {data["stim"][int(peak_firing_index[i])]}')

# Plot the histogram
plt.figure(figsize=(20, 8))
for i in range(Neuron_Num):
    data_temp1 = data[f'neuron{i+1}'][:,int(peak_firing_index[i])]
    data_temp2 = data[f'neuron{i+1}'][:,int(peak_firing_index[i]+4)%data['stim'].shape[0]] 

    plt.subplot(2, 4, i+1) 
    plt.hist(data_temp1 ,bins=20)
    plt.xlabel(f'Firing rate (Hz) at the peak, firing angle {data["stim"][int(peak_firing_index[i])]} ')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of neuron {i+1}')
    plt.text(0.05, 0.95, f'mean: {np.mean(data_temp1):.2f}, std: {np.std(data_temp1):.2f}', transform=plt.gca().transAxes)

    plt.subplot(2, 4, i+5) 
    plt.hist(data_temp2,bins=20)
    plt.xlabel(f'Firing rate (Hz) off the peak, firing angle {data["stim"][int(peak_firing_index[i]+4)%data['stim'].shape[0]]} ')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of neuron {i+1}')
    plt.text(0.05, 0.95, f'mean: {np.mean(data_temp2):.2f}, std: {np.std(data_temp2):.2f}', transform=plt.gca().transAxes)

plt.tight_layout()
plt.draw()
plt.savefig(os.path.join(os.path.dirname(__file__), 'firing_rate_histogram.png'))
plt.close() # Close the figure internally so memory doesn't explode

# Note: We can check if the neuron is a Poisson-like neuron with the criteria E(aX) = aE(X), and Var(aX) = a^2Var(x).
# From the results of mean and std at different tuning angles, Neuron3 is not a Poisson-like neuron.



#### Study 2 ####

# In Study 2, we have 4 neurons stimulated by an unknown stimulus.
# We need to decode the stimulus.

FILENAME2 = os.path.join(os.path.dirname(__file__), 'pop_coding_3.4.pickle')

with open(FILENAME2, 'rb') as f:
    data2 = pickle.load(f)

print(data2.keys())
print(data2['c1'].shape)
print(data2['r1'].shape)

# There are keys: ['c1', 'r1', 'c2', 'r2', 'c3', 'r3', 'c4', 'r4']
# c denotes the vector of neurons, r denotes the firing rate when the unknown stimulus was presented.

# Determine if data['r1'], data['r2'], data['r3'], data['r4'] need to be normalized.
print(data2['c1']) 
print(data2['c2'])
print(data2['c3'])
print(data2['c4'])

print(data2['r1']) 
print(data2['r2'])
print(data2['r3'])
print(data2['r4'])

# Normalize the data by using peak_firing_rate
normalized_data2 = {}
mean_firing_rate = np.zeros((Neuron_Num,))

for i in range(Neuron_Num):
    normalized_data2[f'r{i+1}'] = data2[f'r{i+1}']/peak_firing_rate[i]
    mean_firing_rate[i] = np.mean(normalized_data2[f'r{i+1}'])
    
mean_firing_rate = mean_firing_rate/np.sum(mean_firing_rate)
print(mean_firing_rate)
    
# Calculate the population vector

pop_vector = 0.0
for i in range(Neuron_Num):
    pop_vector += mean_firing_rate[i]*data2[f'c{i+1}']

angle = (np.degrees(np.arctan2(pop_vector[1], pop_vector[0]))*-1+90)%360
# Re-define the coordinate system. y=0 is 0, x=1 is 90.

print(np.degrees(np.arctan2(pop_vector[1], pop_vector[0])))
print(f'the population vector is {pop_vector}, angle is {angle}')

