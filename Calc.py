#Ask them if want to stop after 3
#Be able to accept decimals (use floats)
#Power a number
#Ask for random number
from random import randint

times = 0
maxTimes = 3
play = True
valAnswer = False
valOp = True

while play:
  answer1 = int(input("Do you want to enter a number or get a random number\n Pick 1 for enter or pick 2 for random: "))
  
  if answer1 > 2 or answer1 < 0:
    print('This is not an option.\nPlease select 1 or 2')
  elif answer1 == 1:
    num1 = int(input('What first number do you want to enter: '))
    num2 = int(input('What second number do you want to enter: '))
    valAnswer = True
  elif answer1 == 2:
    for times in range(maxTimes):
      range1 = int(input("Give the start number for the range: "))
      range2 = int(input('Give the last number for the range: '))
      num1 = randint(range1, range2)
      print(num1)

  while valAnswer and times < maxTimes:
    valOp = True
    op = input("What operation do you want to do?\n Do all of the below:\n+\n-\n*\n/\n")
    if op == '+':
      print('Your final function is', num1, '+', num2)
      print('Your final answer is ', num1+num2)
    elif op == '-':
      print('Your final function is', num1, '-', num2)
      print('Your final answer is ', num1-num2)
    elif op == '*':
      print('Your final function is', num1, '*', num2)
      print('Your final answer is ', num1*num2)
    elif op == '/':
      print('Your final function is', num1, '/', num2)
      print('Your final answer is ', num1/num2)
    else:
      print('This is not a valid option please try again')
      valOp = False
    if valOp:
      times+=1

  playAgain = int(input('If you want to play again press 1, otherwise press any other number: '))

  if playAgain != 1:
    play = False
  else:
    times = 0