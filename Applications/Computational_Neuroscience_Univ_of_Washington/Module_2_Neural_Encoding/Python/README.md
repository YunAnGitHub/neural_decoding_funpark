Created by: Yun-An Huang
Date: 2026-Jan-16

# Module 2: Neural Encoding (Python)

This directory contains the exercises and implementations for Module 2 of the Computational Neuroscience course.
The code was edited by Yun-An for testing, and visualizing neural spikes.
The goal of this exercise is to calculate the **Spike-Triggered Average (STA)** of the stimulation given to neurons that elicits spikes.

## File Descriptions
* `main.py`: The primary script for executing the neural encoding models.
* `compute_sta.py`: Core algorithm implementation of the **Spike-Triggered Average (STA)**.
* `c1p8_3.4.pickle`: The dataset used for exercises, containing recorded neuronal activity. It was provided by Rob de Ruyter van Steveninck from a fly H1 neuron responding to an approximate white-noise visual motion stimulus. Data were collected for 20 minutes at a sampling rate of 500 Hz. In the file, rho is a vector that gives the sequence of spiking events or nonevents at the sampled times (every 2 ms). When an element of rho is one, this indicates the presence of a spike at the corresponding time, whereas a zero value indicates no spike. The variable stim gives the sequence of stimulus values at the sampled times. Calculate and plot the spike-triggered average from these data over the range from 0 to 300 ms (150 time steps). (Based on a problem from Sebastian Seung.)