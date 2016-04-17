# dice
Code for Matt Parker's Three Indistinguishable Dice Puzzle

https://www.youtube.com/watch?v=xHh0ui5mi_E
https://www.reddit.com/r/math/comments/4eltj8/the_three_indistinguishable_dice_puzzle/
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
