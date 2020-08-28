#Exercise4.5

from z3 import *

u = DeclareSort('U') # declaring new sort
c = Const('c', u ) # declaring a constant of the sort
f = Function('f', u , u ) # declaring a function of the sort

# declaring a predicate of the sort

P = Function('P', u , BoolSort())
phi = And(f(c) == c, P(f(c)))
solve(phi)

print('c comes out to be U!Val!0, a constant sort.') 
print('The function f(x) returns c for x = c, and returns c for x != c, implying it is a constant function.')
print('The Predicate P(x) returns true for x = c and True for x != c, implying it is a constant predicate that always evaluates to True.')
print('These assignments solve our phi')
