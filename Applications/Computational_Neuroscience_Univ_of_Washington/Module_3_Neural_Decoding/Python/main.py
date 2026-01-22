# this script is to study how to figure out the threshold between two distribution
# Date: 2026-Jan-22
# Author: Yun-An Huang

# the first distribution S1 = N(5,0.5) , S2 = N(7,1) , cost of mistaken think it is S2 is double (more punish in false alarm)
# Q1 

import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.stats as stats

# create two distribution

X = np.arange(0, 10, 0.005)
Y_s1 = stats.norm.pdf(X, 5, 0.5)
Y_s2 = stats.norm.pdf(X, 7, 1)

# calculate the cost
Total_cost = np.zeros((len(X),))
for  i , x in enumerate(X):
    Total_cost[i] = np.sum(Y_s1[i:])*2 + np.sum(Y_s2[:i])

min_cost = np.min(Total_cost)
min_cost_idx = np.argmin(Total_cost)

# plot the two distribution

plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(X, Y_s1)
plt.plot(X, Y_s2)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Two distributions')
plt.legend(['S1', 'S2'])

plt.subplot(2, 1, 2)
plt.plot(X, Total_cost)
plt.xlabel('x')
plt.ylabel('Total cost')
plt.title('Total cost')
plt.axvline(x=X[min_cost_idx], color='r', linestyle='--')
plt.text(X[min_cost_idx], min_cost, f'Threshold: {X[min_cost_idx]:.2f}')

plt.tight_layout()
plt.show()
#