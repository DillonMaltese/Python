board = []
xTurn = True
winner = False
inputX = 0
inputY = 0
chose = False
shape = 'x'

#Adds - to board
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append("-")

while not winner:
    #prints board
    for i in range(3):
        print()
        for j in range(3):
            print(board[i][j], end = " ")


    # for row in board:
    #     print()
    #     for space in row:
    #         print(space, end = " ")

    while not chose:
        inputX = int(input('Please enter the x coordinate you would like to move to\n'))
        inputY = int(input('Please enter the y coordinate you would like to move to\n'))

        if inputX <= 3 and inputX >= 1 and inputY <= 3 and inputY >= 1:
            