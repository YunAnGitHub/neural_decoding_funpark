# Neural Decoding: Tuning Curves and Population Vector Coding
This directory contains the exercises and implementations for Module 4 of the Computational Neuroscience course.
This project explores the relationship between stimulus angles and neuronal firing rates. It utilizes a population of four simulated neurons to analyze individual tuning properties and decode unknown stimuli using the **Population Vector Decoders (PVD)** method.

## 📌 Project Overview

The study is divided into two primary analyses:

1.  **Individual Neuron Analysis:**
    * Generation of **Tuning Curves** to identify the preferred stimulus for each neuron.
    * Statistical analysis of firing rate distributions (Mean vs. Variance) to assess Poisson-like behavior.
    * Identification of peak firing rates and peak firing angles.

2.  **Stimulus Decoding:**
    * Implementation of the **Population Vector Algorithm**.
    * Normalization of firing rates based on individual neuron peaks.
    * Vector summation to predict the angle of an unknown stimulus.

---

## 📊 Methodology

### Tuning Curves
For each neuron, the mean firing rate is calculated across multiple trials for various stimulus angles. 


### Population Vector Decoding
The stimulus angle is predicted by treating each neuron's preferred direction as a vector $\vec{c}_i$ and weighting it by its normalized firing rate $r_i$:

$$\text{PopVector} = \sum_{i=1}^{N} w_i \vec{c}_i$$

The final angle is then derived from the resulting vector using the four-quadrant inverse tangent function ($\text{arctan2}$) and mapped to the specific coordinate system of the experiment.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* NumPy
* Matplotlib
* Pickle (standard library)

### File Structure
* `tuning_analysis.py`: Main script containing both Study 1 and Study 2.
* `tuning_3.4.pickle`: Training data containing stimulus angles and firing rates.
* `pop_coding_3.4.pickle`: Test data containing vectors and response rates for decoding.

