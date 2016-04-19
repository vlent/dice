# Using a throw of three dice to emulate a throw of two.
# Problem posed by Matt Parker during his
# Maths and Stats Society talk  at UWE (2016-04-07 Wed).
# Matt showed a toy with three dice in a transparant cube.
# He asked whether there would be a nice way to use a single
# throw of the three dice to emulate throwing two dice.
#
# I had a brief chat with Tarim after the talk.
# He suggested that if you could do two coloured dice, i.e.,
# two consective throws, then you can also do a single throw of
# two indistinguishable dice.
#
# The idea is to sort the values of the three dice,
# then map this to the range 0 to 35 and
# then map this to two values from 1 to 6
# (using dividend and remainder after division by 6).
# Each (1,1,1), ..., (6, 6, 6) has a 1/216 chance and maps to 0.
# (1,2,2) and (1,1,2) each have a 3/216 chance and map to the same value.
# Similarly other throws with two repeats are taken to be equivalent.
# All throws (excluding those with three repeats and taking into account
# the equivalency for the ones with two repeats) have a chance of 6/216
# and are numbered by consecutive integers.

"""
i = 6
j | 6
--+---
6 | 0

i = 5
k\j| 5 6
---+-----
 6 | 1 1
 5 | 0

i = 4
k\j| 4 5 6
---+-------
 6 | 3 2 3
 5 | 4 4
 4 | 0

i = 3
k\j| 3 4 5 6
---+---------
 6 | 8 6 5 9
 5 | 9 7 9
 4 | A
 3 | 0

...

"""
# update for simpler formula
"""
k = 1
i\j| 1
---+---
 1 | 0

k = 2
i\j| 1 2
---+-----
 1 | 1 1
 2 |   0

k = 3
i\j| 1 2 3
---+-------
 1 | 2 4 2
 2 |   3 3
 3 |     0

k = 4
i\j| 1 2 3 4
---+---------
 1 | 5 A 8 5
 2 |   6 9 6
 3 |     7 7
 4 |       0

...
"""

import random

def tri(n):
    """triangular number"""
    return n*(n+1)//2

def tet(n):
    """tetrahedral number"""
    return n*(n+1)*(n+2)//6


def num_old(triple):
    """convert throw of three dice into number from 0 to 35 uniformly"""
    i, j, k = sorted(triple)
    if i == j == k:
        return 0
    if j == k:
        j = i
    return tet(5-i) + tri(5-j) + 5-k + 2

def num(triple):
    """convert throw of three dice into number from 0 to 35 uniformly"""
    i, j, k = sorted(triple)
    if i == j == k:
        return 0
    else:
        if i == j:
            j = k
        return tet(k-2) + tri(j-2) + i

def topair(triple):
    """convert throw of three dice into throw of two dice uniformly"""
    m = num(triple)
    return (m//6+1, m%6+1)

# compressed solution
def topair_(triple):
    i, j, k = sorted(triple)
    if i == j == k: return (1, 1) # m = 0
    if i == j: j = k # m = (k-2)*(k-1)*(k+3)//6 + i
    m = (k-2)*(k-1)*k//6 + (j-2)*(j-1)//2 + i # tet(k-2)+tri(j-2)+i
    return (m//6+1, m%6+1)

# lookup table
def lookup_table():
    ms = range(6+1)
    row1 = " | ".join([ "%d%d" % (m//6, m%6) for m in ms ])
    ms = [ tri(n) for n in range(5) ]
    row2 = " | ".join(["  "]*2+[ "%d%d" % (m//6, m%6) for m in ms ])
    ms = [ tet(n) for n in range(5) ]
    row3 =  " | ".join(["  "]*2+[ "%d%d" % (m//6, m%6) for m in ms ])
    print(row1)
    print(row2)
    print(row3)

# Solution proposed by David Miller in comments for YouTube video by Matt Parker.
# Does not work.
"""
111 0 11 1
112 1 12
113 2 11 3
114 0 14
115 1 15
116 2 11 3

166 1 16
266 2 26
366 0 66 3
466 1 46
566 2 56
666 3 66 1
"""
def topair2(triple):
    s = sorted(triple)
    t = sum(s) % 3
    del s[t]
    return tuple(s)

# solution proposed by Joey Cole
# with modification based on picking method by David Miller
# doesn't work (original relies on labelling and mod is biased)
def topair3(triple, pick=None):
    if pick is None:
        pick = sum(triple)%3
        triple = sorted(triple)
    return (sum(triple)%6+1, (sum(triple)+triple[pick])%6+1)

# Alexander Nielsen
# doesn't work, similar to David Miller
def topair4(triple):
    s = sorted(triple)
    t = (sum(s)%6)//2
    del s[t]
    return tuple(s)

# doesn't work (requires labelling the dice)
def topair5(triple):
    #s = sorted(triple)
    s = triple
    return ((s[0]+s[1])%6 + 1, (s[1]+s[2])%6 + 1)

"""
lhyan 560728
Here are some rules that work and give the exact probability of a 2D6

- for any n:
(n,n,n) -> (1,1)
- for n>1:
(1,1,n) or (1,n,n) -> (n,n)
- for n>1, m>1 and m<>n:
(n,n,m) -> (1,n)
- for p<n<m, p=1 or 2
(p,n,m) -> (n,m)
- for 2<p<n<m
(p,n,m) -> (2,n+m+p-9)﻿
"""
def topair6(triple):
    p, n, m = sorted(triple)
    if p == n == m:
        return (1, 1)
    if m > 1 and (p == n == 1 or p == 1 and n == m):
        return (m, m)
    if p > 1 and m > 1 and p != m and p == n:
        return (1, p)
    if p == 1 or p == 2:
        return (n, m)
    return (2, n+m+p-9)

# from comment on previous by unekdoud
# Works! (3 indistinguishable to 2 indistinguishable)
def topair7(triple):
    a, b, c = sorted(triple)
    if a==c: return (1,1)
    if a==b or b==c:
        if a==1: return (c,c)
        else: return (1,b)
    if a<=2: return (b,c)
    return (2,a+b+c-9)

topair = topair_

def test_num():
    r6 = range(1, 6+1)
    for i in r6:
        print (i, i, i), num((i, i, i))
    for i_ in range(5):
        i = 5-i_
        for j_ in range(i_+1):
            j = 5-j_
            for k_ in range(j_+1):
                k = 6-k_
                if i == j:
                    print((i, j, k), num((i, j, k)), (i, k, k), num((i, k, k)))
                else:
                    print((i, j, k), num((i, j, k)))

def test_num_():
    r6 = range(1, 6+1)
    for i in r6:
        print (i, i, i), num((i, i, i))
    for k in range(1, 6):
        for j in range(1, k+1):
            for i in range(1, j+1):
                if i == j:
                    print((i, j, k), num((i, j, k)), (i, k, k), num((i, k, k)))
                else:
                    print((i, j, k), num((i, j, k)))

def simulate(N):
    countpairs = [ [0]*6 for _ in range(6) ]
    for _ in range(N):
        throw = [ random.randint(1, 6) for _ in range(3) ]
        a, b = topair(throw)
        countpairs[a-1][b-1] += 1
    return countpairs

if __name__ == "__main__":
    r6 = range(1, 6+1)
    triples = [ (i, j, k) for i in r6 for j in r6 for k in r6 ]
    ms = list(map(num, triples))
    print(sorted(ms))
    count = [0]*36
    for m in ms:
        count[m] += 1
    print(count)
    pairs = list(map(topair, triples))
    print(list(pairs))
    paircount = [ [0]*6 for _ in r6 ]
    for (a, b) in pairs:
        paircount[a-1][b-1] += 1
    print(paircount)
    simpaircount = simulate(36*5000)
    print(simpaircount)
