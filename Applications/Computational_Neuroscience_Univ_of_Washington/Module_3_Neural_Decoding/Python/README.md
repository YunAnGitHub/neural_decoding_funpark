Created by: Yun-An Huang
Date: 2026-Jan-22

# Module 3: Neural Decoding (Python)

This directory contains the exercises and implementations for Module 3 of the Computational Neuroscience course.
The code was edited by Yun-An for testing and visualizing signal detection theory concepts.
The goal of this exercise is to determine the optimal decision threshold between two probability distributions to minimize a specific cost function.

## File Descriptions
* `main.py`: The primary script that:
    * Generates two Gaussian distributions ($S1$ and $S2$).
    * Calculates the total cost of classification errors across a range of thresholds, applying a higher penalty for false alarms (mistaking $S1$ for $S2$).
    * Visualizes the probability density functions and the cost curve to identify the minimum cost threshold.