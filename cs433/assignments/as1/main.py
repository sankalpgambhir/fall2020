#!/bin/python3

from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication
import sys

def is_expr_linear(expr, vars):
    for x in vars:
        for y in vars:
            try: 
                if not Eq(diff(expr, x, y), 0):
                    return False
            except TypeError:
                return False
    return True

def main(inp):
    try:
        transformations = standard_transformations + (implicit_multiplication,)
        expr = parse_expr(inp, transformations=transformations)
    except:
        print('Parse error!')
        return None
    
    var = list(expr.free_symbols)

    if not is_expr_linear(expr, var):
        return False
    elif expr.is_constant():
        return [expr]
    else:
        ret = list(reversed((Poly(expr).coeffs())))
        return ret

if __name__ == '__main__':
    res = main(sys.argv[1])

    if res is False:
        print('Non linear function >:/')
    else:
        print(res)