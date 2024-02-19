from pyquil import get_qc, Program
from pyquil.gates import CNOT, H, MEASURE

qvm = get_qc('2q-qvm')  # Use a 2-qubit quantum virtual machine
p = Program()
p += H(0)  # Apply Hadamard gate to qubit 0
p += CNOT(0, 1)  # Apply CNOT gate between qubits 0 and 1
ro = p.declare('ro', 'BIT', 2)  # Declare classical memory
p += MEASURE(0, ro[0])  # Measure qubit 0
p += MEASURE(1, ro[1])  # Measure qubit 1
p.wrap_in_numshots_loop(10)  # Repeat the experiment 10 times

results = qvm.run(p).get_register_map()['ro'].tolist()
print(results)
