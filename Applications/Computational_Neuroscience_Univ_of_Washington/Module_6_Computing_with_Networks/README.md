# Module 6: Computing with Networks

This folder contains Python scripts for simulating neuronal networks and synaptic interactions.

## Files


### 1. `alpha_neuron_YA1.py`
*   **Description:** Extends `alpha_neuron.py` to study the effect of synaptic time constants.
*   **Key Features:**
    *   Varies the time to peak ($t_{peak}$) of the alpha function.
    *   Observes the relationship between $t_{peak}$ and the total spike count.
    *   Saves plots of the alpha function and spike trains for different $t_{peak}$ values.

### 2. `recurrent_YA.py`
*   **Description:** Solves for the steady-state activity of a recurrent neural network.
*   **Key Features:**
    *   Defines a network with weight matrix $W$, input $u$, and recurrent matrix $M$.
    *   Calculates the steady state $v$ using an iterative loop.
    *   Verifies the result using eigenvalue decomposition and the geometric series formula for gain ($1/(1-\lambda)$).

