from constraints import *
from create_layers import *
import runnn

if __name__ == '__main__':
    layers = create_layers()[2:]
    #raw_input = create_input()[0]
    #input_vector = raw_input[1:]
    #correct_answer = raw_input[0]
    correct_answer, input_vector = runnn.runnn(layers)

    print("Violation occurs at epsilon = ", check_model(layers, input_vector, int(correct_answer)))