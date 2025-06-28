class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def toString(self):
        value = self.value
        if value == 1:
            value = "Ace"
        elif value == 11:
            value = "Jack"
        elif value == 12:
            value = "Queen"
        elif value == 13:
            value = "King"
        return f"{value} of {self.suit}"