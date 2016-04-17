# information/entropy of dice

#import numpy as np
import sympy

def info(ps, base=2):
    return -sum(p*sympy.log(p, base) for p in ps)

def distinguishableinfo(ds, base=2):
    return sum(sympy.log(d, base) for d in ds)

def count(f, ds):
    cs = {}
    def rec(ds, t):
        if len(ds) == 0:
            s = f(t)
            cs[s] = cs.get(s, 0) + 1
        else:
            for val in range(1, ds[0]+1):
                rec(ds[1:], t + [val])
    rec(ds, [])
    return cs

def indistinguishablecounts(n, d):
    return count(lambda t: tuple(sorted(t)), [d]*n)

# def indistinguishablecounts_(n, d):
#     cs = {}
#     def rec(i, t):
#         if i == n:
#             s = tuple(sorted(t))
#             cs[s] = cs.get(s, 0) + 1
#         else:
#             for val in range(1, d+1):
#                 rec(i+1, t + [val])
#     rec(0, [])
#     return cs

def indistinguishableinfo(n, d, base=2):
    cs = indistinguishablecounts(n, d)
    ps = [ sympy.sympify(c)/d**n for c in cs.values() ]
    return info(ps, base)

def sumcounts(ds):
    return count(lambda t: sum(t), ds)

def suminfo(ds, base=2):
    cs = sumcounts(ds)
    N = sympy.prod(ds)
    ps = [ sympy.sympify(c)/N for c in cs.values() ]
    return info(ps, base)

if __name__ == "__main__":
    b = 6
    print
    #simp = sympy.simplify
    #simp = sympy.nsimplify
    simp = sympy.expand
    cases = [("D", lambda n: distinguishableinfo([6]*n, b)),
             ("I", lambda n: indistinguishableinfo(n, 6, b)),
             ("S", lambda n: suminfo([6]*n, b))]
    results = {}
    for n in range(1, 3+1):
        for label, func in cases:
            B = func(n)
            print "%d%s6 : %.2f" % (n, label, B), simp(B*sympy.log(6)*36*3)
