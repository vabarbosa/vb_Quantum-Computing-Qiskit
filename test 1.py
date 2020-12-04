from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(6, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.cx(qreg_q[1], qreg_q[0])
circuit.cx(qreg_q[3], qreg_q[4])
circuit.cx(qreg_q[2], qreg_q[0])
circuit.y(qreg_q[1])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[4], qreg_q[0])
circuit.y(qreg_q[1])
circuit.z(qreg_q[4])
circuit.cx(qreg_q[5], qreg_q[2])
circuit.measure(qreg_q[0], creg_c[0])