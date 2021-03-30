def getIntegerInput(prompt):
  while True:
    try:
      userInput = int(input(prompt))       
    except ValueError:
      print("Not an integer! Try again.")
      continue
    else:
      return userInput 
      break

def boardDisplay(x):
  for i in range(len(x)):
    
    print(i + 1, end="")
    print(" ", end="")
  print()