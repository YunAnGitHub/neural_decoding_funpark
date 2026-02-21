"""
Created by Yun-An Huang
Date: 2026-Feb-20

Script to demonstrate Oja's rule and Hebbian learning on 2D datasets.
It explores how these algorithms behave with centered vs. non-centered data
and compares the learned weights to the principal components (eigenvectors).

Data: 
    'c10p1.pickle': Dictionary containing 100 (x,y) data points.

"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
from hebbian_algorithm import hebbian_algorithm
from oja_algorithm import oja_algorithm


DIR = os.path.dirname(__file__)
FigDir = os.path.join(DIR,'fig')

# initialize
if not os.path.exists(FigDir):
    os.makedirs(FigDir)


# Load data from pickle file
Data_Path  = os.path.join(DIR, 'c10p1.pickle')
with open(Data_Path, 'rb') as f:
    data_temp = pickle.load(f)


# Extract data array
print(data_temp.keys) 
data = data_temp['c10p1']

print(data.shape)
#print(data)

# Plot the raw data
plt.figure(1)
plt.scatter(data[:,0], data[:,1]) 
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Scatter plot of raw data")
plt.savefig(os.path.join(FigDir, f'c10p1_x_y_scatter.png'))
plt.close()

# Center the data (subtract mean) so that the mean is (0,0).
# This is crucial for Oja's rule to converge to the first Principal Component.
data_nor = np.zeros((data.shape))
data_nor = data - np.mean(data, axis=0)


# Plot the centered data
plt.figure(2)
plt.scatter(data_nor[:,0], data_nor[:,1]) 
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Scatter plot of centered data")
plt.savefig(os.path.join(FigDir, f'c10p1_x_y_scatter_nor.png'))
plt.close()

# Calculate the correlation matrix (covariance matrix since mean is 0).
# The eigenvectors of this matrix correspond to the Principal Components.
X_cor = np.dot(data_nor.T,data_nor)/data.shape[0]
eig_val, eig_vec = np.linalg.eig(X_cor)



# Question 1: Observe the convergence of weights (w) for Oja's algorithm 
# when data is centered. It should align with the principal eigenvector.
print("\n--- Question 1: Centered Data ---")

print(f"Eigenvalues:\n {eig_val}")
print(f"Eigenvectors:\n {eig_vec}")

print("\n--- Oja's Algorithm on centered Data ---")
oja_algorithm(data_nor)
os.system("pause")

print("\n--- Hebbian Algorithm on centered Data ---")
hebbian_algorithm(data_nor)
os.system("pause")

# Question 2: Investigate the effect of non-centered data.
# We shift the centered data by a constant vector to see how it affects learning.
print("\n--- Question 2: Shifted (Non-centered) Data ---")

#shf_value = np.random.rand(1,2)*3
shf_value = [0.2 ,0.3]
data_shf = np.zeros((data.shape))
data_shf = data - np.mean(data, axis=0) + shf_value

X_cor_shf = np.dot(data_shf.T,data_shf)/data.shape[0]
eig_val, eig_vec = np.linalg.eig(X_cor_shf )

print(f"Mean of data after shifting: {np.mean(data_shf, axis=0)}")
print(f"Eigenvalues: {eig_val}")
print(f"Eigenvectors: \n {eig_vec}")
print(f"Shift value applied: {shf_value}")

print("\n--- Oja's Algorithm on Shifted Data ---")
oja_algorithm(data_shf)
os.system("pause")

print("\n--- Hebbian Algorithm on Shifted Data ---")
hebbian_algorithm(data_shf)


# Question 3: Theoretical analysis of Hebbian learning direction.
# Calculate eigenvectors for a specific correlation matrix Q to compare 
# with theoretical expectations.
print("\n--- Question 3: Theoretical Matrix Q ---")
Q = [[0.15, 0.1],[0.1,0.12]]
print(f"Matrix Q:\n{Q}")

eig_v_Q, eig_vec_Q = np.linalg.eig(Q)

print(f"Eigenvalues: {eig_v_Q}")
print(f"Eigenvectors: \n {eig_vec_Q}") 