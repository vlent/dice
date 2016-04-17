# threetotwodice
#
# Maps three identical dice to two individual dice with the correct
# distribution.
#
# Posed by Matt Parker at UWE Maths and Stats Society talk 2016-04-07.
#
# Inspired to create a simpler solution which might fit in a tweet and write it
# in Python by Jan Van Lent (but Python still feels such a messy language).
#
#
# This solution maps to two individual dice, (say red and blue) but could be
# simplified if this doesn't matter by combining two lines in topair to:
#     if a == b or b == c or b-a == 1: return (a, c)
#
# The (sum minus constant) in the solution can result in 0 or -1 which both map
# to 1.  This only happens in one case when (-1,0) maps to (1,1).


import numpy
def face( x ):
    """ Return a value contrained to range 1 to 6 """
    return numpy.clip( x, 1, 6 )


def topair( triple ):
    """
    Convert a triple dice to a pair of dice
        all the same -> (6, 6)
        two the same -> (high, low)
        low, middle differ by 1 -> (low, high)
        middle, high differ by 1 -> (sum-9, sum-8)
        otherwise -> (sum-7, sum-7)
    """
    a, b, c = sorted( triple )

    if a == b == c: return (6, 6)

    if a == b or b == c: return (c, a)

    if b-a == 1: return (a, c)

    s = sum( triple )
    if c-b == 1: return (face( s-9 ), face( s-8 ))

    return (s-7, s-7)
    

if __name__ == "__main__":
    r6 = range( 1, 6+1 )
    triples = [ (a, b, c) for a in r6 for b in r6 for c in r6 ]
    paircount = dict( ((p, q), 0) for p in r6 for q in r6 )

    print "Mappings:"
    for triple in triples:
        pair = topair( triple )
        paircount[pair] += 1
        print triple, pair

    print "Distribution:"
    for pair in sorted( paircount ):
        print pair, paircount[pair]