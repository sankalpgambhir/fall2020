#Exercise4.5

from z3 import *

x = BitVec('x', 4)
y = BitVec('y', 4)

phi = And(x + y < 0, x > 0, y > 0)
print(phi)

solve(phi)
