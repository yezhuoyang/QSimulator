import numpy as np



def fidelity(statevector1, statevector2):
    """Compute the fidelity between two statevectors."""
    return np.abs(np.vdot(statevector1, statevector2))**2



class Simulator:
    def __init__(self):
        pass



    def simulate(self, qasm_str: str):
        """
            Simulate the circuit implemented by the input qasm string qasm_str. 

            Return the statevector in numpy array format of that qasm str.

            Please use Little endian encoding.
        
        """
        pass
