from constraints import *
from create_layers import *

if __name__ == '__main__':
    layers = create_layers()
    raw_input = create_input()[0]
    input_vector = raw_input[1:]
    correct_answer = raw_input[0];
    
    print("Violation occurs at epsilon = ", check_model(layers, input_vector, correct_answer))