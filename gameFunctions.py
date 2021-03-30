winner = ""
def isThereAWin(gameState):
  # checks for a winner
  
  return isThereAWinInAnyRow(gameState) or isThereAWinInAnyColumn(gameState) or isThereAWinInADiagonal(gameState)

def isThereAWinInAnyRow(gameState):
  # checks for a winner in any row
  global winner
  # checking for x wins

  # top row
  if gameState[0] == 1 and gameState[1] == 1 and gameState[2] == 1:
    print("Player O wins in the top row")
    winner = "O"
    return True
    
  # middle row
  if gameState[3] == 1 and gameState[4] == 1 and gameState[5] == 1:
    print("Player O wins in the middle row")
    winner = "O"
    return True
    
  # bottom row
  if gameState[6] == 1 and gameState[7] == 1 and gameState[8] == 1:
    print("Player O wins in the bottom row")
    winner = "O"
    return True
  
  # checking for o wins

  # top row
  if gameState[0] == -1 and gameState[1] == -1 and gameState[2] == -1:
    print("Player X wins in the top row")
    winner = "X"
    return True 

  # middle row
  if gameState[3] == -1 and gameState[4] == -1 and gameState[5] == -1:
    print("Player X wins in the middle row")
    winner = "X"
    return True
    
  if gameState[6] == -1 and gameState[7] == -1 and gameState[8] == -1:
    print("Player X wins in the bottom row")
    winner = "X"
    return True
    
  # no winner in any row
  return False

def isThereAWinInAnyColumn(gameState):
  # checks for a winner in any column
  global winner
  # checking for x wins

  # left column
  if gameState[0] == 1 and gameState[3] == 1 and gameState[6] == 1:
    print("Player O wins in the left column")
    winner = "O"
    return True

  if gameState[1] == 1 and gameState[4] == 1 and gameState[7] == 1:
    print("Player O wins in the middle column")
    winner = "O"
    return True
    
  if gameState[2] == 1 and gameState[5] == 1 and gameState[8] == 1:
    print("Player O wins in the right column")
    winner = "O"
    return True
  
  if gameState[0] == -1 and gameState[3] == -1 and gameState[6] == 1:
    print("Player X wins in the left column")
    winner = "X"
    return True
    
  if gameState[1] == -1 and gameState[4] == -1 and gameState[7] == -1:
    print("Player X wins in the middle column")
    winner = "X"
    return True

  if gameState[2] == -1 and gameState[5] == -1 and gameState[8] == -1:
    print("Player X wins in the right column")
    winner = "X"
    return True
  # no winner in any column
  return False

def isThereAWinInADiagonal(gameState):
  global winner
  
  if gameState[0] == 1 and gameState[4] == 1 and gameState[8] == 1:
    print("Player O wins in the diagonal starting from the top left")
    winner = "O"
    return True
    
  if gameState[2] == 1 and gameState[4] == 1 and gameState[6] == 1:
    print("Player O wins in the diagonal starting from the top right")
    winner = "O"
    return True

  if gameState[0] == -1 and gameState[4] == -1 and gameState[8] == -1:
    print("Player X wins in the diagonal starting from the top left")
    winner = "X"
    return True

  if gameState[2] == -1 and gameState[4] == -1 and gameState[6] == -1:
    print("Player X wins in the diagonal starting from the top right")
    winner = "X"
    return True
  
  return False

def isThereADraw(gameState):
  if gameState.count(0) == 0 and isThereAWin(gameState) == False:
    return True
  return False

def gameStateUI(gameState):
  print(str(gameState[0:3]) + "\n" + str(gameState[3:6])+ "\n" + str(gameState[6:9]))

def print2DBoard(gameState):
  boardStateConversion = {
    -1 : "X",
    0 : "-",
    1 : "O"
  }
  #boardState = gameState[]
  print ((boardStateConversion[gameState[0]]) + " | " + (boardStateConversion[gameState[1]]) + " | " + (boardStateConversion[gameState[2]]))
  print("---------")
  print ((boardStateConversion[gameState[3]]) + " | " + (boardStateConversion[gameState[4]]) + " | " + (boardStateConversion[gameState[5]]))
  print("---------")
  print ((boardStateConversion[gameState[6]]) + " | " + (boardStateConversion[gameState[7]]) + " | " + (boardStateConversion[gameState[8]]))