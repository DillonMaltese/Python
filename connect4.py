winner = False
bTurn = True
board = []
input = 0
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
        input = int(input('What column would you like to go into\n'))

        if input < 8 and input > 0:
            #Making gravity
            for i in range(6):
                if board[input][6 - i] == "-":
                    board[input][6 - i]  = shape

                    if shape == "b":
                        shape = "r"
                    else:
                        shape = "b"

                    boardFull += 1
                    chose = True

        else: 
            print("invalid spot")


