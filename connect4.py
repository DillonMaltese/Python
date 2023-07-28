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

        if inputRow < 8 and inputRow >= 0:
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


    # for x in range(4):
    #     for y in range(6):
    #         print(x+3)
    #         if board[x][y] == board[x+1][y] and board[x][y] == board[x+2][y] and board[x][y] == board[x+3][y]:
    #             if board[x][y] == "b":
    #                 print("Blue won")
    #                 winner = True

    #             elif board[x][y] == "r":
    #                 print("Red won")
    #                 winner = True

    # for x in range(7):
    #     for y in range(4):
    #         if board[x][y] == board[x][y+1] and board[x][y] == board[x][y+2] and board[x][y] == board[x][y+3]:
                # if board[x][y] == "b":
                #     print("Blue won")
                #     winner = True

                # elif board[x][y] == "r":
                #     print("Red won")
                #     winner = True


    # for x in range(4):
    #     for y in range(4):
    #         if board[x][y] == board[x+1][y+1] and board[x][y] == board[x+2][y+2] and board[x][y] == board[x+3][x+3]:
    #             if board[x][y] == "b":
    #                 print("blue won")
    #                 winner = True

    #             elif board[x][y] == "r":
    #                 print("Red won")
    #                 winner = True



    # if not winner and boardFull == 42:
    #     print("There is a tie")
    #     winner = True




    #Horizontal check
for x in range(4):
    for y in range(6):
        if board[x][y] == board[x+1][y] and board[x][y] == board[x+2][y] and board[x][y] == board[x+3][y]:
            # Rest of the code
            if board[x][y] == "b":
                print("Blue won")
                winner = True

            elif board[x][y] == "r":
                print("Red won")
                winner = True

#Vertical check
for x in range(7):
    for y in range(3):
        if board[x][y] == board[x][y+1] and board[x][y] == board[x][y+2] and board[x][y] == board[x][y+3]:
            # Rest of the code
            if board[x][y] == "b":
                print("Blue won")
                winner = True

            elif board[x][y] == "r":
                print("Red won")
                winner = True

#Diagonal check (bottom-left to top-right)
for x in range(4):
    for y in range(3):
        if board[x][y] == board[x+1][y+1] and board[x][y] == board[x+2][y+2] and board[x][y] == board[x+3][y+3]:
            # Rest of the code
            if board[x][y] == "b":
                print("Blue won")
                winner = True

            elif board[x][y] == "r":
                print("Red won")
                winner = True

#Diagonal check (top-left to bottom-right)
for x in range(4):
    for y in range(3, 6):
        if board[x][y] == board[x+1][y-1] and board[x][y] == board[x+2][y-2] and board[x][y] == board[x+3][y-3]:
            # Rest of the code
            if board[x][y] == "b":
                print("Blue won")
                winner = True

            elif board[x][y] == "r":
                print("Red won")
                winner = True