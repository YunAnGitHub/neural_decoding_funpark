
"""
Created by Yun-An Huang
Date: 2026-Feb-20

Implementation of Hebbian learning rule.
Note: Basic Hebbian learning is unstable as weights can grow without bound.

Args:
    data (np.ndarray): Input data array of shape (N, 2).
"""

import numpy as np

def hebbian_algorithm(data):
    """
    Executes Hebbian learning on the provided dataset.
    
    Updates weights based on the correlation between input and output:
    dw/dt = eta * v * u
    """

    w0 = np.random.randn(2, 1) # initialize weights randomly
    w_prev = None
    w_th = 1e-7     # Convergence threshold
    err = np.inf    # Error metric (change in weights)

    # Hyperparameters
    eta = 1         # Learning rate
    alpha = 1       # Unused in basic Hebbian (used in Oja's)
    delta_t = 0.01  # Time step size
    
    count = 0       # Data index counter
    epoch = 20      # Total number of epochs to run
    epoch_count = 0 # Current epoch counter

    while epoch_count < epoch and err > w_th:
        if w_prev is None:
            w_prev = w0
        
        # Get current input vector u
        u = data[count,:]
        u = u.reshape(2,1)  
        
        # Calculate output v = w^T * u (linear neuron)
        v = np.dot(w_prev.T, data[count,:])

        # Hebbian update rule: dw = eta * v * u * dt
        # Weights increase if input (u) and output (v) are correlated.
        w = w_prev + delta_t*eta*(v*u)
        
        # Calculate magnitude of weight change
        err = np.linalg.norm(w - w_prev)
        w_prev = w
        count += 1
        
        # Check if end of dataset reached (end of epoch)
        if count == data.shape[0]:
            count = 0
            epoch_count += 1
            if epoch_count % 5 == 0:
                print(f"Epoch {epoch_count}: error (delta w) is {err}")
                print(f"Epoch {epoch_count}: Current weight vector: \n {w}")
    
    print("Final weight vector:", w)