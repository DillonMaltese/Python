#Goes from top to bottom
#Last on = First off
#Like a deck of cards
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.sizeCount = 0

    def printStack(self):
        for i in range(self.sizeCount):
            print(self.stack[self.sizeCount - 1 - i])

    def push(self, element):
        if self.sizeCount == self.size:
            raise ValueError("Stack is full. Cannot push more elements.")
        else:
            self.stack.append(element)
            self.sizeCount += 1

    # #Removes the top number of the stack if not empty
    def pop(self):
        if self.sizeCount == 0:
            raise ValueError("Stack is empty. Cannot remove an element")
        else:
            del self.stack[self.sizeCount-1]
            self.sizeCount -= 1


    # #Prints the top of the stack without removing
    def peak(self):
        if self.sizeCount == 0:
            return None
        
        return self.stack[self.sizeCount - 1]

