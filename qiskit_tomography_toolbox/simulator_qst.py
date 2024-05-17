import numpy as np
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit
from .base_tomography import BaseTomography


class SimulatorQST(BaseTomography):
    def __init__(self, circuit: QuantumCircuit):
        """Simulator based QST.
        Args:
            circuit (QuantumCircuit): The circuit
        """
        self.circuit = circuit
        self.num_qubits = circuit.num_qubits

    def get_relative_amplitude_sign(self, parameters: np.ndarray):
        """Get the relative amplitude signes between the amplitudes.

        Args:
            parameters (np.ndarray): parameters of the circuits
        """
        state_vector = (
            Statevector(self.circuit.assign_parameters(parameters))
        ).data.real
        return np.sign(state_vector)

    def get_statevector(
        self, parameters: np.ndarray, **kwargs
    ):  # pylint: disable=unused-argument
        """Get the state vector of the circuit.
        Args:
            parameters (np.ndarray): parameters of the circuits
        """
        return (Statevector(self.circuit.assign_parameters(parameters))).data.real
