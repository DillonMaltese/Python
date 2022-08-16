xTurn = True
winner = False
spacesFull = 0
rows, columns = (3, 3)
board = [[0]*columns]*rows

#Printing the board
while winner is False :
    if xTurn == True :
        print("It is X's turn")
        xTurn == True
    if xTurn == False :
        print("It is O's turn")
        xTurn = True
    winner = True
