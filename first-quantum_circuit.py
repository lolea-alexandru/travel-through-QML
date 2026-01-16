# The following code is based on the tutorial by PennyLane
# Source: https://www.youtube.com/watch?v=uCm027_jvZ0

# ================= IMPORTS ================= #
import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# ================= QUANTUM CIRCUIT ================= #
# Register the quantum device (simulator in this case) and specify the number of qubits (wires)
dev = qml.device("default.qubit", wires=2)


# Pennylane automatically sets the qubits in the 0 state => we can directly start with our operations
@qml.qnode(dev)  # Encapsulate the device together with the circuit
def first_circuit(theta):
    qml.PauliX(wires=1)
    qml.CNOT(wires=[1, 0])
    qml.RY(theta, wires=0)

    return qml.expval(qml.PauliZ(wires=0))


# print(first_circuit(np.pi))

# ================= PLOT ================= #
# Define the range of angles
thetas = np.arange(-np.pi, np.pi, 0.01)

# Create the array with measurements
measurements = np.zeros(len(thetas))

for i, theta in enumerate(thetas):
    measurements[i] = first_circuit(theta)

# Plot the measurements
plt.plot(thetas, measurements)
plt.show()
