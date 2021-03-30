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

  print("hello, game is started...")

  # local constants

  # general constants
  SENTINEL = -2

  # local variables

  # game variables
  gameInPlay = True
  prompt = "Enter a value between 1 and 9 (" + str(SENTINEL + 1) + " to quit): "

  
  debug = False
  
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

    gameFunctions.print2DBoard(gameState)
    #ioFunctions.boardDisplay(gameState)
    numTurns += 1

    if numTurns % 2 == 1:
      OTurn = True
      while OTurn:
        userInput = (ioFunctions.getIntegerInput(prompt) - 1)
        if userInput == SENTINEL:
          break
        elif not (userInput > -1 and userInput < 9):
          print("invalid input " + str(userInput))
        elif not gameState[userInput] == 0:
          print("invalid input " + str(userInput) + ". That space is already taken")
        else:
          gameState[userInput] = 1
          print("processing move by player O")
          currentPlayer = "X"
          break
    else:
      XTurn = True
      while XTurn:
        userInput = (ioFunctions.getIntegerInput(prompt) - 1)
        if userInput == SENTINEL:
          break
        elif not (userInput > -1 and userInput < 9):
          print("invalid input " + str(userInput))
        elif not gameState[userInput] == 0:
          print("invalid input " + str(userInput) + ". That space is already taken")
        else:
          gameState[userInput] = -1
          print("processing move by player X")
          currentPlayer = "O"
          break

    if gameFunctions.isThereAWin(gameState) and gameFunctions.winner == "O":
      print(gameFunctions.blue)
      gameFunctions.printWinningBoard(gameState)
      print(gameFunctions.white)
      break

    if gameFunctions.isThereAWin(gameState) == True and gameFunctions.winner == "X":
      print(gameFunctions.red)
      gameFunctions.printWinningBoard(gameState)
      print(gameFunctions.white)
      break

    if gameFunctions.isThereADraw(gameState):
      print("there is a draw")
      break
    else:
      print("there is not a winner")

    if currentPlayer == "X":
      print("It is player X's turn.")

    if currentPlayer == "O":
      print("It is player O's turn.") 
  
  print("goodbye, game is over")

##### main

if __name__ == "__main__":
  main()