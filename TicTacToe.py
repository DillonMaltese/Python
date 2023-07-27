board = []
xTurn = True
winner = False
inputX = 0
inputY = 0
chose = False
shape = 'x'
boardFull = 0

#Adds - to board
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append("-")

while winner == False:
    chose = False
    #prints board
    for j in range(3):
        print()
        for i in range(3):
            print(board[i][j], end = " ")


    # for row in board:
    #     print()
    #     for space in row:
    #         print(space, end = " ")

    while chose == False:
        inputX = int(input('Please enter the x coordinate you would like to move to\n'))
        inputY = int(input('Please enter the y coordinate you would like to move to\n'))

        if inputX <= 2 and inputX >= 0 and inputY <= 2 and inputY >= 0:
            if board[inputX][inputY] == "-":
                board[inputX][inputY] = shape
                if shape == 'x':
                    shape = 'o'
                else:
                    shape = 'x'
                boardFull += 1
                chose = True
            else:
                print("You can't go there")

    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'x':
            print('x won')
            winner = True
        elif board[0][0] == 'o':
            print('o won')
            winner = True

    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[2][0] == 'x':
            print('x won')
            winner = True
        elif board[2][0] == 'o':
            print('o won')
            winner = True
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == 'x':
            print('x won')
            winner = True
        elif board[0][0] == 'o':
            print('o won')
            winner = True

    elif board[1][0] == board[1][1] and board[1][1] == board[2][1]:
        if board[1][0] == 'x':
            print('x won')
            winner = True
        elif board[1][0] == 'o':
            print('o won')
            winner = True

    elif board[0][2] == board[1][2] and board[2][2] == board[1][2]:
        if board[0][2] == 'x':
            print('x won')
            winner = True
        elif board[0][2] == 'o':
            print('o won')
            winner = True

    elif board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == 'x':
            print('x won')
            winner = True
        elif board[0][0] == 'o':
            print('o won')
            winner = True

    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] == 'x':
            print('x won')
            winner = True
        elif board[1][0] == 'o':
            print('o won')
            winner = True

    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] == 'x':
            print('x won')
            winner = True
        elif board[2][0] == 'o':
            print('o won')
            winner = True

    elif boardFull == 9:
        print("There is a tie")
        winner = True

