# QSimulator

This is the homework template for quantum circuit simulator for CS238.


Your simulator should be able to compile any qasm file with the following gate sets: x,h,t,cx,tdg.


We will test your simulator by calling:

```
Simulator.simulate(qasm_str)
'''

The expected output is a complex numpy array which encodes the final quantum state vector. For example, for the following qasm file


```
OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];
x q[0]
'''

The output should be quantum state |100>, which is encoded as:

```
[0.+0.j 1.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
'''

We will test the fidelity of your output by the following function:

```
def fidelity(statevector1, statevector2):
    """Compute the fidelity between two statevectors."""
    return np.abs(np.vdot(statevector1, statevector2))**2
'''


# What should you submit?


On gradescope, please submit a single python file simulator.py. You are only allowed to use numpy package. Any other imported python package will be 
seen as cheating. 

If your implementation contain multiple functions, please put them in the same simulator.py file.
