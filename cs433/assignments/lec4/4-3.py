#Exercise4.3
from z3 import *

A = Bool("A")
B = Bool("B")
C = Bool("C")

D = Or(And(A,B),Not(Or(Or(B,C),And(A,C))))
print(D)

s = Solver()
s.add(D)
r = s.check()

if r == sat:
    print("Sat")
    m = s.model()
    print(m)
else:
    print("Unsat")
