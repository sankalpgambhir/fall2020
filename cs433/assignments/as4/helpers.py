import z3
import numpy as np

def rectify(x):
    assert (type(x) == z3.z3.ArithRef), "Attempted to rectify non arithref object"
    return z3.If(x > 0, x, 0)

def vecrectify(x):
    return [rectify(i) for i in x]

def vecsum(x, y):
    assert (len(x) == len(y)), "Attempted incompatible vector addition"
    return [(x[i] + y[i]) for i in range(len(x))]

def lintrans(W, v):
    # returns Wv for a matrix W and vector v
    assert (len(W) == len(v)), "Incompatible matrix operation"
    return [sum([W[i][j]*v[j] for i in range(len(W))]) for j in range(len(W[0]))]

def constrain_input(inp_z3, inp_real, epsilon):
    assert (len(inp_z3) == len(inp_real)), "Incompatible input vectors for constraints"
    assert (epsilon >= 0), "Negative perturbation provided! Bounded constraints"
    if(epsilon == 0):
        return z3.And([inp_z3[i] == inp_real[i] for i in range(len(inp_z3))])
    else:
        return z3.And([z3.Or((inp_z3[i] > inp_real[i] + epsilon), (inp_z3[i] < inp_real[i] - epsilon)) for i in range(len(inp_z3))])
    
    assert 0, "Invalid flow of control"
    pass

def check_epsilon(solver, inp_z3, inp_real, epsilon):
    solver.push() # assure old contraints aren't affected
    solver.add(constrain_input(inp_z3, inp_real, epsilon))
    if(solver.check() == z3.sat):
        solver.pop()
        return True
    else:
        solver.pop()
        return False
