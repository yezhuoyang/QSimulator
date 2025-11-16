# QSimulator

This repository contains the starter template for the Quantum Circuit Simulator assignment in CS 238: Quantum Programming.

Your task is to implement a simulator that parses and executes OpenQASM 2.0 circuits using a restricted gate set. At the end of simulation, your code should return the final quantum state vector as a NumPy complex array.


Your simulator should be able to compile any qasm file with the following gate sets: x,h,t,cx,tdg.



# Simulation API

You should implement a class called Simulator, please don't change the name. We will test your simulator by calling:

```python
Simulator.simulate(qasm_str)
```

The input is a string containing a valid QpenQASM 2.0 program.

Output is a 1-dimensional NumPy array of complex numbers representing the final statevector in computational basis order. We use exactly the same encoding as qiskit.

```
OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];
x q[0]
```

The output should be quantum state |100>, which is encoded as:

```python
[0.+0.j 1.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
```

We will test the fidelity of your output by the following function:

```python
def fidelity(statevector1, statevector2):
    """Compute the fidelity between two statevectors."""
    return np.abs(np.vdot(statevector1, statevector2))**2
```


# Simulation Instructions


On gradescope, please submit a single python file simulator.py. You are only allowed to use numpy package. Any other imported python package will be 
seen as cheating. 

If your implementation contain multiple functions, please put them in the same simulator.py file.

