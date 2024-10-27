# Schrödinger's Cat Simulation
This program uses Qiskit to simulate the famous thought experiment by Erwin Schrödinger, illustrating the concept of quantum superposition.

## Overview

In this simulation, we create a quantum circuit that represents Schrödinger's Cat, which exists in a superposition of being both alive and dead until measured. By applying quantum gates, we manipulate the probabilities of these states.

## Requirements

Ensure you have the following libraries installed:

```plaintext
qiskit
qiskit-aer
qiskit-ibm-runtime
matplotlib
```

'## Code Summary

The main components of the code include:

- **Initialization**: Setting up the quantum circuit with one qubit representing the cat's state.
- **Quantum Gates**: Using the Hadamard gate to create superposition and the rotation gate (RY) to manipulate probabilities.
- **Measurement**: Measuring the qubit to observe the state of the cat.
- **Visualization**: Plotting the results to show the probabilities of the cat being alive or dead (Saved as image).

## Running the Simulation

To run the simulation, execute the following command:

```bash
python schrodingers_cat.py
