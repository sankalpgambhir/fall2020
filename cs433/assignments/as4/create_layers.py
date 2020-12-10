import os.path
import numpy as np
import pandas as pd

def create_layers():
    dirname = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(dirname, "models/mnist_relu_3_50.tf")

    tf_file = open(filename, 'r')
    tf_file_stuff = tf_file.read()
    layer_list = tf_file_stuff.split("\n")

    layers = []
    i = 0

    while i < len(layer_list):
        if (layer_list[i] != "ReLU"):
            break
        else:
            (w,b) = (eval(layer_list[i+1]), eval(layer_list[i+2]))
            w = np.array(w)
            b = np.array(b).reshape(-1,1)
            layers.append((w,b))
            i += 3
    
    return layers

def create_input():
    dirname = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(dirname, "data/mnist_test.csv")

    dframe = pd.read_csv(filename)
    return np.array(dframe)

