import numpy as np
from cmath import exp
from math import pi, sin, cos
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

angles = {"theta": pi / 2, "phi": 0}

#set up the bit and qubit vectors

ket_0 = "|0\u27e9"
ket_1 = "|1\u27e9"

bits = {
    "bit = 0": {"theta": 0, "phi": 0},
    "bit = 1": {"theta": pi, "phi": 0},
    ket_0 : {"theta": 0, "phi": 0},
    ket_1: {"theta": pi, "phi": 0},
    ket_0 + ' + ' + ket_1: angles,
} 


qbits = []
for b in bits:
    bloch = (
        cos(bits[b]["phi"]) * sin(bits[b]["theta"]),
        sin(bits[b]["phi"]) * sin(bits[b]["theta"]),
        cos(bits[b]["theta"])
    )


    #plot_bloch_vector(bloch, title=b)
    #plt.show()
    #qbits.append(bloch)

     # Build the state vector
    a = cos(bits[b]["theta"] / 2)
    b = exp(bits[b]["phi"] * 1j) * sin(bits[bit]["theta"] / 2)
    state_vector = [a * complex(1, 0), b * complex(1, 0)]
    print("State vector:", np.around(state_vector, decimals=3))
