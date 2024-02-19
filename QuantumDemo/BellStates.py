from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare

p = Program(
    Declare("ro", "BIT", 2),
    H(0),
    CNOT(0, 1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(10)

# run the program on a QVM
qc = get_qc('9q-square-qvm')
result = qc.run(qc.compile(p)).get_register_map().get("ro")
print(result[0])
print(result[1])