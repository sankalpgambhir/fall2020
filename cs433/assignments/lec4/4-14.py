from z3 import *

def solve(phi):
    s = Solver()
    s.add(phi)
    res = s.check()
    print(res)
    if res == sat:
        print(s.model())
    
    return res

def main_a():
    blue = Function('blue', IntSort(), BoolSort()) # is object blue?
    black = Function('black', IntSort(), BoolSort()) # is object black?

    sky, space, x = Ints('sky space x')

    color_constraint = ForAll(x, Not(And(blue(x), black(x)))) # can only be one color
    sky_prop = blue(sky)
    space_prop = black(space)

    conclusion = And(Or(blue(sky), black(sky)), Or(blue(space), black(space)))

    phi = And(color_constraint, sky_prop, space_prop, Not(conclusion))
    
    if solve(phi) == unsat:
        print("Sky and Space are each blue or black, theorem holds true")
    else:
        print("Theorem fails under given model")

    return 0

def main_b():
    rugged = Function('rugged', IntSort(), BoolSort()) # is object rugged?
    prof = Function('prof', IntSort(), BoolSort()) # is object a prof tool?
    vehicle = Function('vehicle', IntSort(), BoolSort()) # is object a vehicle?
    hammer, chainsaw, n, m = Ints('hammer chainsaw n m')

    rugged_constraint = ForAll(n, Implies(Or(prof(n), vehicle(n)), rugged(n)))
    tools_constraint = And(prof(hammer), prof(chainsaw))

    to_check = rugged(hammer)

    phi = And(rugged_constraint, tools_constraint, Not(to_check))

    if solve(phi) == unsat:
        print("Hammers are rugged, theorem holds true")
    else:
        print("Theorem fails under given model")

    return 0


if __name__ == '__main__':
    main_a()
    main_b()