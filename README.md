### Tic Tac Toe with 1D List Project
*by Ryan Rothermel*



X is represented by 1
O is represented by -1
blank/empty square is represented by 0

For example, the TTT board

```
O | O | -
---------
X | X | O
---------
- | X | -

```

would be represented with the tic tac toe board entries 'peeled off' from top-down, left-right (row major, column minor) to fill the one-dimensional list variable `gameState` as in

`gameState = [1, 1, 0, -1, -1, 1, 0, -1, 0]`

or

```
gameState = [
  1, 1, 0, # top row (positions 0, 1 & 2)
  -1, -1, 1, # middle row (positions 3, 4, & 5)
  0, -1, 0  # bottom row (positions 6, 7, & 8)
  ]```
```

This version of Tic Tac Toe is multiplayer. One user plays as O and X is played by the other player. Turns alternate and use the same system of input.

If the user inputs a position that is either already taken or out of the index, their turn will restart rather than switch to the other player.

If a draw is detected by the program, the game will end in a draw.