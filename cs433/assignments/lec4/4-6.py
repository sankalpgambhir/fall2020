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
    x, y = Reals('x y')
    g = Function('g', RealSort(), RealSort(), RealSort())
    
    xy_constraint = (x == y)
    g_constraint = And(g(x, y) < 0, g(y, x) > 0)

    phi = And(xy_constraint, g_constraint)

    solve(phi)

    return 0


if __name__ == '__main__':
    main()