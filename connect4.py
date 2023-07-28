winner = False
bTurn = True
board = []
inputRow = 0
shape = 'b'
boardFull = 0

#Set board to empty
for i in range(6):
    board.append([])
    for j in range(7):
        board[i].append("-")

#While there is no winner yet
while not winner:
    chose = False
    #Printing board
    for i in range(6):
        print()
        for j in range(7):
            print(board[i][j], end = " ")

    while not chose:
        #Finding the column to go into
        inputRow = int(input('\nWhat column would you like to go into\n'))

        if inputRow < 8 and inputRow > 0:
            #Making gravity
            for i in reversed(range(6)):
                print(i)
                if board[i][inputRow] == "-":
                    board[i][inputRow]  = shape

                    if shape == "b":
                        shape = "r"
                    else:
                        shape = "b"

                    boardFull += 1
                    chose = True
                    break

        else: 
            print("invalid spot")


