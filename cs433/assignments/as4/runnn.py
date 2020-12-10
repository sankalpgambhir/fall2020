import numpy as np

def rectify(X):
   return np.maximum(0,X)

def runnn(layers):
    inp = np.random.rand(np.shape(layers[0][0])[1])
    #inp = inp * 255
    vec = inp
    for l in layers:
        vec = rectify(np.dot(l[0], vec) + l[1])
    
    if np.count_nonzero(vec) == 0:
        return runnn(layers)
    else:
        return np.amax(vec), inp