def topair(triple):
    i, j, k = sorted(triple)
    if i == j == k: return (1, 1) # m = 0
    if i == j: j = k
    m = (k-2)*(k-1)*k//6 + (j-2)*(j-1)//2 + i # tet(k-2)+tri(j-2)+i
    return (m//6+1, m%6+1)

if __name__ == "__main__":
    r6 = range(1, 6+1)
    triples = [ (i, j, k) for i in r6 for j in r6 for k in r6 ]
    pairs = list(map(topair, triples))
    print(sorted(list(pairs)))
    paircount = [ [0]*6 for _ in r6 ]
    for (a, b) in pairs:
        paircount[a-1][b-1] += 1
    print(paircount)
