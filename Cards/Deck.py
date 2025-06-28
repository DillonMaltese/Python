from Card import Card
from random import randint

class Deck:
    def __init__(self):
        self.deck = []
        
        for v in range(1, 14):
            for s in range(1, 4):
                if s == 1:
                    self.deck.append(Card(v, "Hearts"))
                elif s == 2:
                    self.deck.append(Card(v, "Diamonds"))
                elif s == 3:
                    self.deck.append(Card(v, "Clubs"))
                else:
                    self.deck.append(Card(v, "Spades"))
                    
    def shuffle(self):
        #For every element in the array, swap it with another element
        for i in range(len(self.deck)):
            #Setting x to a random number between i and the length of the deck
            x = randint(i, len(self.deck) - 1)
            temp = self.deck[i]
            self.deck[i] = self.deck[x]
            self.deck[x] = temp
            
    def draw(self):
        return self.deck.pop()
    
    def getLength(self):
        return len(self.deck)