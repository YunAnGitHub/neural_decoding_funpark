"""
Created by Yun-An Huang
Date: 2026-Feb-17

1. Calculate the recurrent loop.

"""
from __future__ import print_function, division
import numpy as np
from scipy.linalg import circulant

# Initialization
steps = 100

W = 0.5 * np.eye(5) + 0.1 * np.ones((5, 5))
u = [[0.6],[0.5],[0.6],[0.2],[0.1]]
M = circulant([-0.25, 0, 0.25, 0.25, 0])

print(W)
print(u)
print(M)    

# Using a loop to solve the equation
v = np.zeros((5,1))
for step in range(steps):

    # Calculate v
    v = np.dot(W,u) + np.dot(M,v)
    print(v)


# Using eigenvalues and eigenvectors to solve the equation
# Vss = sum( cc_1*1/(1-lambda_1)*eig_vec_1 + cc_2*1/(1-lambda_2)*eig_vec_2 ..... + cc_n*1/(1-lambda_n)*eig_vec_n)

v_in = np.dot(W,u) # Constant input
print(v_in)

eig_val, eig_vec = np.linalg.eig(M) # Eigenvalues and eigenvectors of matrix M
cc = np.linalg.solve(eig_vec,v_in) # The representation of v_in using eigenvectors: eig_vec * cc = v_in
print(cc)

eig_val = eig_val[:,np.newaxis] # Extend the array to two dimensions
gains = 1/(1-eig_val) # The 1/(1-lambda) gain term of the amplifier 
v_ss = np.dot(eig_vec,gains*cc) # Vss = sum( cc_1*1/(1-lambda_1)*eig_vec_1 + cc_2*1/(1-lambda_2)*eig_vec_2 ..... + cc_n*1/(1-lambda_n)*eig_vec_n)

print(v_ss)