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
    x, y, z = Reals('x y z')
    z_constraint = (z == (3*x + 2*y - 3))
    assertion = Implies(y > 0, Not(z == 0))

    phi = And(z_constraint, Not(assertion)) # assertion fails

    solve(phi)

    return 0


if __name__ == '__main__':
    main()