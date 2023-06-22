import random

gameOver = False
botAnswer = ''
playAnswer = ''


def player(pAnswer):
    pAnswer = input('Do you want Rock Paper or Scissors\nChoose r, p, or s\n')


def bot(bAnswer):
    num = random.randint(1, 3)
    if num == 1:
        bAnswer = 'r'
    elif num == 2:
        bAnswer = 'p'
    elif num == 3:
        bAnswer = 's'
    print("The bot chose " + bAnswer)


while not gameOver:
    playAnswer = input('Do you want Rock Paper or Scissors\nChoose r, p, or s\n')
    bot(botAnswer)
    print(playAnswer)
    if playAnswer == 'r' and botAnswer == 's' or playAnswer == 'p' and botAnswer == 'r' or playAnswer == 's' and botAnswer == 'p':
        print('You won')
    elif botAnswer == 'r' and playAnswer == 's' or botAnswer == 'p' and playAnswer == 'r' or botAnswer == 's' and playAnswer == 'p':
        print('The bot won')
    playAgain = input('Would you like to play again\nSay y or n\n')
    if playAgain == 'n':
        gameOver = False


