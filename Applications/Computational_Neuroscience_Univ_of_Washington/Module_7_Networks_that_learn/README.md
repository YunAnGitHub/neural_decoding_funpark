# Module 7: Networks that Learn

This directory contains implementations of unsupervised learning algorithms, specifically **Hebbian Learning** and **Oja's Rule**, as part of the Computational Neuroscience course.

## Files

*   **`oja_YA.py`**: The main execution script. It performs the following:
    *   Loads and visualizes 2D data points.
    *   Centers the data (subtracts mean).
    *   Computes the correlation matrix and its eigenvectors (Principal Components).
    *   Runs Oja's and Hebbian algorithms to demonstrate weight convergence.
    *   Compares results on centered vs. non-centered data.
*   **`oja_algorithm.py`**: Contains the function `oja_algorithm(data)` which implements Oja's rule ($dw/dt = \eta (v u - \alpha v^2 w)$).
*   **`hebbian_algorithm.py`**: Contains the function `hebbian_algorithm(data)` which implements basic Hebbian learning ($dw/dt = \eta v u$).

## Usage

Run the main script to observe the learning process:

```bash
python oja_YA.py
```

## Key Observations

1.  **Oja's Rule**: Converges to the first Principal Component (eigenvector with the largest eigenvalue) when data is centered.
2.  **Hebbian Learning**: Unstable without normalization; weights grow indefinitely.
3.  **Data Centering**: Crucial for Oja's rule to act as a PCA extractor.
