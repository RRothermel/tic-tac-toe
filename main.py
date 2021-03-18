# YOUR NAME HERE
# Works Cited
# None

##### imports

import gameFunctions
import ioFunctions

##### global constants


##### global variables
global gameState

##### functions

def main():
  # main game logic

  print("hello, 2 player game is started...")

  # local constants

  # general constants
  SENTINEL = -1

  # local variables

  # game variables
  gameInPlay = True
  prompt = "Enter a value between 0 and 8 (" + str(SENTINEL) + " to quit): "
  
  debug = True
  
  gameState = [
    0, 0, 0, 
    0, 0, 0,
    0, 0, 0
  ]

  numTurns = 0
  while gameInPlay:
    if debug:
      print("debugging...")
      gameFunctions.gameStateUI(gameState)

    ioFunctions.boardDisplay(gameState)
    numTurns += 1
    userInput = ioFunctions.getIntegerInput(prompt)
    # user wants to exit     
    if userInput == SENTINEL:
      break
    elif not (userInput > -1 and userInput < 9):
      print("invalid input " + str(userInput))
    elif not gameState[userInput] == 0:
      print("invalid input " + str(userInput) + ". That space is already taken")
    else:
      if numTurns % 2 == 1:
        gameState[userInput] = 1
        print("processing move by player O")
      else:
        gameState[userInput] = -1
        print("processing move by player X")

      if gameFunctions.isThereAWin(gameState):
        print(gameState)
        break

      if gameFunctions.isThereADraw(gameState):
        print("there is a draw")
        break
      else:
        print("there is not a winner")
  
  print("goodbye, game is over")

##### main

if __name__ == "__main__":
  main()