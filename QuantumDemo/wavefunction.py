import numpy as np
from pyquil import Program
from pyquil.gates import *
from pyquil.api import WavefunctionSimulator
wf_sim = WavefunctionSimulator()
coin_flip = Program(H(0))
print(wf_sim.wavefunction(coin_flip))

coin_flip = Program(H(0))
wavefunction = wf_sim.wavefunction(coin_flip)
print(wavefunction)

assert wavefunction[0] == 1 / np.sqrt(2)
# The amplitudes are stored as a numpy array on the Wavefunction object
print(wavefunction.amplitudes)
prob_dict = wavefunction.get_outcome_probs() # extracts the probabilities of outcomes as a dict
print(prob_dict)
prob_dict.keys() # these store the bitstring outcomes
assert len(wavefunction) == 1 # gives the number of qubits