# Module 5: Computing in Carbon

This folder contains Python scripts simulating basic neuron models, specifically the passive membrane and the Integrate-and-Fire (I&F) model.

## Files

### 1. `membrane.py`
*   **Description:** Simulates the charging and discharging curves of a passive membrane patch.
*   **Key Features:**
    *   Calculates the theoretical time constant ($\tau = RC$).
    *   Simulates membrane potential $V$ over time using the Euler method.
    *   Verifies the time constant experimentally from the simulation.

### 2. `intfire.py`
*   **Description:** Implements a basic Integrate-and-Fire neuron model to determine the rheobase.
*   **Key Features:**
    *   Iterates through increasing input currents ($I$).
    *   Simulates membrane potential until a spike occurs ($V > V_{th}$).
    *   Identifies the minimum input current required to elicit a spike.
    *   Generates plots for voltage traces.

### 3. `intfire_noise.py`
*   **Description:** Extends the I&F model by adding Gaussian noise to the input current.
*   **Key Features:**
    *   Simulates the neuron under different noise amplitudes.
    *   Records spike times and calculates inter-spike intervals (ISI).
    *   Plots voltage traces and ISI histograms to analyze the effect of noise.

## Usage

Run the scripts using Python:

```bash
python membrane.py
python intfire.py
python intfire_noise.py
```
