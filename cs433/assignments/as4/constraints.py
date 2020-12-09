import numpy as np
from helpers import *

def check_model(layer, input_vector, correct_ans):
    # generate solving context

    sol = z3.Solver()

    # get layer = [ [W, b], [W, b], ... ]
    layer_z3 = []

    # convert to z3 and constrain
    for i in range(len(layer)):
        w, b = layer[i]
        
        w_z = [[z3.Int("w" + "_" + str(i) + "_" + str(j) + "_" + str(k)) for j in range(np.shape(w)[0])] for k in range(np.shape(w)[1])]
        b_z = [z3.Int("b" + "_" + str(i) + "_" + str(j)) for j in range(np.shape(b)[0])]
        
        w_z_const = z3.And([(w_z[j][k] == w[j][k]) for j in range(np.shape(w)[0]) for k in range(np.shape(w)[1])])
        b_z_const = z3.And([(b_z[j] == b[j]) for j in range(np.shape(b)[0])])

        sol.add(w_z_const, b_z_const)

        layer_z3.append([w_z, b_z])

        pass

    inp = [z3.Int("i_" + str(j)) for j in range(np.shape(layer[0][0])[1])]

    # constraint input by layer
    sol.add(constrain_input(inp, input_vector, 0))

    # contains result of each layer, last element at the end is the output
    res = [inp]

    for l in layer_z3:
        res.append(vecrectify(vecsum(lintrans(l[0], res[-1]), b)))

    sol.add(z3.And([res[-1][correct_ans] > res[-1][i] for i in range(len(res[-1])) if i != correct_ans]))

    return None
