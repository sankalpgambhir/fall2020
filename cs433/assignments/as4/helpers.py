import z3
import numpy as np

z3.set_param('parallel.enable', True)
z3.set_param("verbose", 10)

def rectify(x):
    assert (type(x) == z3.z3.ArithRef), "Attempted to rectify non arithref object"
    return z3.If(x > 0, x, 0)

def vecrectify(x):
    return [rectify(i) for i in x]

def vecsum(x, y):
    assert (len(x) == len(y)), ("Attempted incompatible vector addition " + str(len(x)) + " " + str(len(y)))
    return [(x[i] + y[i]) for i in range(len(x))]

def lintrans(W, v):
    # returns Wv for a matrix W and vector v
    assert (len(W[0]) == len(v)), "Incompatible matrix operation"
    return [sum([W[j][i]*v[i] for i in range(len(W[0]))]) for j in range(len(W))]

def constrain_input(inp_z3, inp_real, epsilon):
    assert (len(inp_z3) == len(inp_real)), ("Incompatible input vectors for constraints " + str(len(inp_z3)) + " " + str(len(inp_real)))
    if(epsilon == 0):
        return z3.And([inp_z3[i] == inp_real[i] for i in range(len(inp_z3))])
    elif(epsilon > 0):
        return z3.And([z3.Or((inp_z3[i] > inp_real[i] + epsilon), (inp_z3[i] < inp_real[i] - epsilon)) for i in range(len(inp_z3))])
    else:
        return z3.And([z3.And((inp_z3[i] > inp_real[i] + epsilon), (inp_z3[i] < inp_real[i] - epsilon)) for i in range(len(inp_z3))])
    
    assert 0, "Invalid flow of control"
    pass

def check_epsilon(solver, inp_z3, inp_real, epsilon):
    solver.push() # assure old contraints aren't affected
    solver.add(constrain_input(inp_z3, inp_real, epsilon))
    solver.add(constrain_input(inp_z3, inp_real, -2*epsilon))
    if(solver.check() == z3.sat):
        solver.pop()
        return True
    else:
        solver.pop()
        return False
