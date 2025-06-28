from Deck import Deck

def sumHand(hand):
    #Aces are special, count them to use later
    aceCount = 0
    sum = 0
    for i in range(len(hand)):
        if (hand[i].value == 1):
            aceCount += 1
            sum += 1
        elif (hand[i].value > 10):
            sum += 10
        else:
            sum += hand[i].value

    #assign the aces favorable point values
    for i in range(aceCount):
        if (sum + 10 <= 21):
            sum += 10

    return sum
    
    
    
def draw(deck):
    if (deck.getLength() == 0):
        deck = Deck()
        deck.shuffle()

    return deck.draw()


playerHand = []
dealerHand = []

playing = True
playerTurn = True

deck = Deck()
deck.shuffle()

while (playing == True):
  
  playerHand = []
  dealerHand = []

  playerTurn = True
  
  playerHand.append(draw(deck))
  playerHand.append(draw(deck))
  dealerHand.append(draw(deck))
  dealerHand.append(draw(deck))

  while (playerTurn == True and sumHand(playerHand) < 21):
    for i in range(len(playerHand)):
      print("Your hand:", playerHand[i].toString())
    choice = input("Would you like to hit or stay?")
    if (choice == "hit"):
      playerHand.append(draw(deck))
      print("Drew:", playerHand[-1].toString())
    elif (choice == "stay"):
      playerTurn = False
    else:
      print("Invalid choice.")

  while (sumHand(dealerHand) < sumHand(playerHand) and \
         sumHand(dealerHand) < 21):
    dealerHand.append(draw(deck))

  if (sumHand(playerHand) == 21):
    print("You got Blackjack!")
  if (sumHand(dealerHand) == 21):
    print("The dealer got Blackjack!")

  if (sumHand(playerHand) > 21):
    print("You busted! You lose!")
  elif (sumHand(dealerHand) > 21):
    print("The dealer busted! You win!")
    for i in range(len(dealerHand)):
      print("Dealer:", dealerHand[i].toString())
  else:
    for i in range(len(dealerHand)):
      print("Dealer:", dealerHand[i].toString())
    if (sumHand(playerHand) < sumHand(dealerHand)):
      print("You lost!")
    else:
      print("You won!")

  choice = input("Would you like to play again?")
  if (choice == "no"):
    playing = False