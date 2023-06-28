from array import *

Board = ['/ ', '/ ', '/ '], ['/ ', '/ ', '/ '], ['/ ', '/ ', '/ ']
winner = False
xTurn = True

def printBoard(Board):
    for x in range(3):
      print(''.join(Board[x]))

def takeInput(Board, xTurn):
  if xTurn == True:
    rowInput = int(input("What row does x want to go into\n"))
    colInput = int(input("What column does x want to go into\n"))
    if(Board[rowInput][colInput] != '/ '):
      print("You can't do that")
      takeInput(Board, xTurn)
    else:
      Board[rowInput][colInput] = 'x '
  else:
    rowInput = int(input("What row does o want to go into\n"))
    colInput = int(input("What column does o want to go into\n"))
    if(Board[rowInput][colInput] != '/ '):
      print("You can't do that")
      takeInput(Board, xTurn)
    else:
      Board[rowInput][colInput] = 'o '

def checkWinner(Board, winner):
  if Board[0][0] and Board[1][1] and Board[2][2] == 'x ' or Board[0][0] and Board[1][1] and Board[2][2] == 'o ':
    if Board[0][0] == 'x ':
      print("X Won!!!")
      winner = True
    else:
      print("Y Won!!!")
      winner = True
  elif Board[0][2] and Board[1][1] and Board[2][0] == 'x ' or Board[0][2] and Board[1][1] and Board[2][0] == 'o ':
    if Board[0][2] == 'x ':
      print("X Won!!!")
      winner = True
    else:
      print("Y Won!!!")
      winner = True
  elif Board[1][0] and Board[1][1] and Board[2][1] == 'x ' or Board[1][0] and Board[1][1] and Board[2][1] == 'o ':
    if Board[1][1] == 'x ':
      print("X Won!!!")
      winner = True
    else:
      print("Y Won!!!")
      winner = True

  else:
      break


while winner == False:
  printBoard(Board)
  takeInput(Board, xTurn)
  xTurn = not xTurn