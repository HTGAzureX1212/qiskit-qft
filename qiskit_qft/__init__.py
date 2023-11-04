from math import pi
from qiskit import QuantumCircuit

def rotations(circuit: QuantumCircuit, n: int) -> QuantumCircuit:
  assert n >= 0

  if n == 0:
    return circuit

  q1 = n - 1
  while q1 >= 0:
    circuit.h(q1)

    for q2 in range(q1):
      circuit.cp(pi / 2**(q1 - q2), q2, q1)

    circuit.barrier()

    q1 -= 1


def swap_all(circuit: QuantumCircuit, n: int):
  for q in range(n // 2):
    circuit.swap(q, n - q - 1)


def qft(circuit: QuantumCircuit, n: int) -> None:
  rotations(circuit, n)
  swap_all(circuit, n)

def inverse_qft(circuit: QuantumCircuit, n: int) -> None:
  temp_circuit = QuantumCircuit(n)
  qft(temp_circuit, n)
  circuit.combine(temp_circuit.inverse())
