import numpy as np
from pyquil import Program
from pyquil.gates import *
from pyquil.api import WavefunctionSimulator

# Create a WavefunctionSimulator object to simulate quantum computations
wf_sim = WavefunctionSimulator()

# Create a quantum program for flipping a coin using a Hadamard gate
coin_flip = Program(H(0))

# Print the wavefunction resulting from the coin flip program
print(wf_sim.wavefunction(coin_flip))

# Reassign the coin flip program to ensure consistent results
coin_flip = Program(H(0))

# Obtain the wavefunction resulting from the coin flip program
wavefunction = wf_sim.wavefunction(coin_flip)
print(wavefunction)

# Check if the probability amplitude of the |0> state is 1/sqrt(2)
assert wavefunction[0] == 1 / np.sqrt(2)

# Print the probability amplitudes stored as a numpy array in the Wavefunction object
print(wavefunction.amplitudes)

# Extract the probabilities of different outcomes as a dictionary
prob_dict = wavefunction.get_outcome_probs()
print(prob_dict)
prob_dict.keys() 

# these store the bitstring outcomes
assert len(wavefunction) == 1 # gives the number of qubits
