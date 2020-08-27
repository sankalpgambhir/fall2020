from z3 import *

def solve(phi):
    s = Solver()
    s.add(phi)
    res = s.check()
    print(res)
    if res == sat:
        print(s.model())
    
    return res

def main():
    drinks = Function('drinks', IntSort(), BoolSort()) # does person n drink?
    n, m = Ints('n m')\

    everyone_drinks = ForAll(n, drinks(n))
    one_drinks = Exists(m, drinks(m))
    phi = Implies(one_drinks, everyone_drinks)

    if solve(Not(phi)) is unsat:
        print('Valid')
    else:
         print('Not valid')

    return 0


if __name__ == '__main__':
    main()