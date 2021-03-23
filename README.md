### Tic Tac Toe with 1D List Project
*by Ryan Rothermel*



X is represented by -1
O is represented by 1
blank/empty square is represented by 0

For example, the TTT board

```
X | X |
---------
X |   |
---------
O | O |
```

would be represented with the tic tac toe board entries 'peeled off' from top-down, left-right (row major, column minor) to fill the one-dimensional list variable `gameState` as in

`gameState = [1, 1, 0, 1, 0, 0, 0, -1, -1]`

or

```
gameState = [
  1, 1, 0, # top row (positions 0, 1 & 2)
  1, 0, 0, # middle row (positions 3, 4, & 5)
  0, -1, -1  # bottom row (positions 6, 7, & 8)
  ]
