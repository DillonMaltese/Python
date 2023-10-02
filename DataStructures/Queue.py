#Goes from bottom to top
#First on = First off
#Like a line
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.sizeCount = 0

    #Prints the queue from first to last
    def printQueue(self):
        for i in self.sizeCount:
            print(self.queue[i])
    
    #Adds a number to the back of the queue
    def enqueue(self, input):
        self.queue[self.sizeCount] = input
        sizeCount += 1
    
    #Takes the first element out of the queue and returns it
    def dequeue(self):
        placeHolder = self.queue[0]
        for i in self.sizeCount - 1:
            self.queue[i] = self.queue[i + 1]

        return placeHolder

    #Prints the element that will first come off of the queue but doesn't remove it
    def peek(self):
        print(self.sizeCount[0])

    #Same as dequeue but just returns nothing if the queue is empty
    def poll():
        