"""

Created by Yun-An Huang
Date: 2026-Feb-20

Implementation of Oja's learning rule to extract the first principal component.

Args:
    data (np.ndarray): Input data array of shape (N, 2).

"""

import numpy as np


# Oja's Algorithm
# implement Oja's algorithm
def oja_algorithm(data):
    """
    Executes Oja's learning on the provided dataset.
    
    Updates weights based on the correlation between input and output:
    dw/dt = eta * (v * u - alpha * v^2 * w)
    """

    w0 = np.random.randn(2, 1) # initialize weights randomly
    w_prev = None   # initial w_prev
    w_th = 1e-7     # Convergence threshold (unused in current loop condition)
    err = np.inf    # Error metric (change in weights)

    # Hyperparameters
    eta = 1         # Learning rate
    alpha = 1       # Forgetting factor (controls weight normalization)
    delta_t = 0.01  # Time step
    
    count = 0       # Data index counter
    epoch = 20      # Number of epochs
    epoch_count = 0 # Current epoch

    while epoch_count < epoch and err > w_th:
        if w_prev is None:
            w_prev = w0
        
        # Calculate output v = w^T * x
        # Using one data point at a time or batch; here we iterate through data
        u = data[count,:]
        u = u.reshape(2,1)  
        v = np.dot(w_prev.T, data[count,:])

        # Oja's rule update: dw/dt = eta * (v * u - alpha * v^2 * w)
        # This rule normalizes the weights while maximizing variance (finding PC1)
        w = w_prev + delta_t*eta*(v*u - alpha*(v**2)*w_prev)
        
        # Calculate weight change
        err = np.linalg.norm(w - w_prev)
        w_prev = w
        count += 1
        
        # count epoch
        if count == data.shape[0]:
            count = 0
            epoch_count += 1
            if epoch_count % 5 == 0:
                print(f"Epoch {epoch_count}: error (delta w) is {err}")
                print(f"Epoch {epoch_count}: Current weight vector: \n {w}")
    
    print("Final weight vector:", w)