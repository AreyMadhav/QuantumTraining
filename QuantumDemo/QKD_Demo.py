from pyquil import Program, get_qc
from pyquil.gates import *
from numpy.random import randint
import numpy as np

# Define the number of qubits and the number of trials
n = 5
trials = 10

# Define the quantum virtual machine
qvm = get_qc(f"{n}q-qvm")

# Define the quantum program
p = Program()

# Alice prepares the qubits
alice_basis = randint(2, size=n) # 0 for computational, 1 for Hadamard
alice_state = randint(2, size=n) # 0 for |0> or |+>, 1 for |1> or |->
for i in range(n):
    if alice_basis[i] == 0: # Use computational basis
        if alice_state[i] == 0: # Prepare |0>
            p += I(i)
        else: # Prepare |1>
            p += X(i)
    else: # Use Hadamard basis
        if alice_state[i] == 0: # Prepare |+>
            p += H(i)
        else: # Prepare |->
            p += X(i)
            p += H(i)

# Bob measures the qubits
bob_basis = randint(2, size=n) # 0 for computational, 1 for Hadamard
ro = p.declare('ro', 'BIT', n) # Declare classical memory
for i in range(n):
    if bob_basis[i] == 0: # Use computational basis
        p += MEASURE(i, ro[i])
    else: # Use Hadamard basis
        p += H(i)
        p += MEASURE(i, ro[i])

# Repeat the experiment for the given number of trials
p.wrap_in_numshots_loop(trials)

# Run the program and get the results
result = qvm.run(p)

# Extract classical memory from the result object
classical_memory = result.get_register_map()['ro']

# Print the results
print(f"Alice's basis: {np.array2string(alice_basis)}")
print(f"Alice's state: {np.array2string(alice_state)}")
print(f"Bob's basis: {np.array2string(bob_basis)}")
print("Results:")
for i in range(trials):
    print(f"Trial {i+1}: {np.array2string(classical_memory[i])}")

