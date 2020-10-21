from z3 import *
import random

max_moves = 6
correct_sequence = [1, 1]

def generate_random_sequence(n, k):
    sequence = []
    for i in range(k):
        rand_int = random.randint(0,n-1)
        sequence.append(rand_int)
    return sequence

def hard_constraints(s, x, a, b, n, k):

    color_cons = And([ And(0 <= x[j], x[j] < n) for j in range(k)])

    s.add(color_cons)
    s.add(a(x) == RealVal(k))
    s.add(b(x) == 0)

    return s

def soft_constraints(s, x, a, b, n, k):

    for i in range(max_moves):
        seq = generate_random_sequence(n, k)
        first = [x[j] == seq[j] for j in range(k)]
        seq_a, seq_b = check_sequence(seq, correct_sequence, k)
        s.add_soft(And([Implies(And(first), a(x) == seq_a), Implies(And(first), b(x) == seq_b)]))
    
    return s

def construct_constraints(s, n, k):

    x = Array('x', IntSort(), IntSort())

    a = Function('a', ArraySort(IntSort(), IntSort()), IntSort())
    b = Function('b', ArraySort(IntSort(), IntSort()), IntSort())

    s = hard_constraints(s, x, a, b, n, k)
    s = soft_constraints(s, x, a, b, n, k)

    return s


def check_sequence(input_sequence, corr, k):
    temp_correct = corr
    in_correct_pos = 0
    in_wrong_pos = 0

    for i in range(k):
        if (input_sequence[i] == temp_correct[i]):
            in_correct_pos += 1
            input_sequence[i] *= -1
            temp_correct[i] *= -1

    for i in range(k):
        if (temp_correct[i] > 0 ):
            try:
                index = input_sequence.index(temp_correct[i])
                in_wrong_pos += 1
                input_sequence[index] *= -1
            except ValueError:
                continue

    return in_correct_pos, in_wrong_pos

if __name__ == '__main__':
    # do things

    n, k = 2, 2

    s = Optimize()

    construct_constraints(s, n, k)

    if s.check() == sat:
        print("A possible solution is:")
        print(s.model())
    else:
        print("No solution found!")

    pass