import Data.List as L

-- sort a triple
sort3' (x, y, z) = (i, j, k)
    where [i, j, k] = L.sort [x, y, z]
-- alternative using sorting network
sort2 (x, y)
  | x > y = (y, x)
  | otherwise = (x, y)
-- x0 --o-----o-- x3
--      |     |
-- y0 --o--o--o-- y3
--         |
-- z0 -----o----- z2
sort3 (x0, y0, z0) = (x3, y3, z2)
  where (x1, y1) = sort2 (x0, y0)
        (y2, z2) = sort2 (y1, z0)
        (x3, y3) = sort2 (x1, y2)
-- count occurrences
count xs = map length $ L.group $ L.sort xs


-- triangular number
tri n = n*(n+1) `div` 2

-- tetrahedral number
tet n = n*(n+1)*(n+2) `div` 6

-- convert throw of three dice into number from 0 to 35 uniformly
num = num' . sort3
num' (i, j, k)
    | (i == j) && (j == k) = 0
    | i == j = num' (i, k, k)
    | otherwise = tet (k-2) + tri (j-2) + i

-- original solution
--    | j == k = num' (i, i, k)
--    | otherwise = tet (5-i) + tri (5-j) + 5-k + 2

-- convert throw of three dice into throw of two dice uniformly
topair triple = (q+1, r+1)
    where (q, r) = divMod (num triple) 6

-- tests
triples = [ (i, j, k) | i <- [1..6], j <- [1..6], k <- [1..6] ]
nums = map num triples
pairs = map topair triples
numcounts = count nums
paircounts = count pairs
