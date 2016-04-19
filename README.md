# dice
Code for [Matt Parker](http://standupmaths.com)'s Three Indistinguishable Dice P

https://www.youtube.com/watch?v=xHh0ui5mi_E
https://www.reddit.com/r/math/comments/4eltj8/the_three_indistinguishable_dice_puzzle/
https://www.reddit.com/r/math/comments/4eltj8/the_three_indistinguishable_dice_puzzle/d2699eb
https://www.reddit.com/r/MattParker/comments/4ek9ow/the_three_indistinguishable_dice_puzzle/
https://www.reddit.com/r/mathriddles/comments/4epcvk/the_three_indistinguishable_dice_puzzle/

Code from threetotwodice_mini.py:
```python
def topair(triple):
    i, j, k = sorted(triple)
    if i == j == k: return (1, 1) # m = 0
    if i == j: j = k
    m = (k-2)*(k-1)*k//6 + (j-2)*(j-1)//2 + i # tet(k-2)+tri(j-2)+i
    return (m//6+1, m%6+1)
```

For hand calculations:

- If all the same: 00
- If two the same: low -> row 1, high -> row 2, high -> row 3
- If all different: low -> row 1, mid -> row 2, high -> row 3

Do addition base 6. Interpret 0 as 6 or add 1 to each digit.

|   |  1 |  2 |  3 |  4 |  5 |  6 |
|---|----|----|----|----|----|----|
| 1 | 01 | 02 | 03 | 04 | 05 | 10 |
| 2 |    | 00 | 01 | 03 | 10 | 14 |
| 3 |    | 00 | 01 | 04 | 14 | 32 |

Examples:
- (3,3,3) -> 00 -> 11
- (2,2,5) -> 02 + 10 + 14 = 30 -> 41
- (1,2,5) -> 01 + 00 + 14 = 15 -> 26
