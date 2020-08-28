#Exercise4.5

from z3 import *

u = DeclareSort('U') # declaring new sort
c = Const('c', u ) # declaring a constant of the sort
f = Function('f', u , u ) # declaring a function of the sort

# declaring a predicate of the sort

P = Function('P', u , BoolSort())
phi = And(f(c) == c, P(f(c)))
solve(phi)
