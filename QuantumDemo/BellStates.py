from pyquil import get_qc, Program
from pyquil.gates import CNOT, H, MEASURE

# Use a 2-qubit quantum virtual machine
qvm = get_qc('2q-qvm')
p = Program()

# Apply Hadamard gate to qubit 0
p += H(0)

# Apply CNOT gate between qubits 0 and 1
p += CNOT(0, 1)

# Declare classical memory
ro = p.declare('ro', 'BIT', 2)
p += MEASURE(0, ro[0])  # Measure qubit 0
p += MEASURE(1, ro[1])  # Measure qubit 1

# Repeat the experiment 10 times
p.wrap_in_numshots_loop(10)

results = qvm.run(p).get_register_map()['ro'].tolist()
print(results)
