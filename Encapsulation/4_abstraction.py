class Stack():
    ''' Stack class implements a last in first out LIFO algorithm'''
    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.dataList = [ ]
        else:
            self.dataList = startingStackAsList[:]  # make a copy 
        
    def push(self, item):       
        self.dataList.append(item)

    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError
        element = self.dataList.pop()
        return element

    def peek(self):
        # Retrieve the top item, without removing it
        item = self.dataList[-1]
        return item

    def getSize(self):
        nElements = len(self.dataList)
        return nElements

    def show(self):
        # Show the stack in a vertical orientation
        print('Stack is:')
        for value in reversed(self.dataList):
            print('   ', value)

oStack = Stack()
oStack.push(5)
oStack.push(12)
oStack.push('Some data')
oStack.push('Some more data')
oStack.push(True)
oStack.show()

while True:
    print()
    item = oStack.pop()
    print('Next value from the stack is:', item)
    if oStack.getSize() == 0:
        break
    oStack.show()

print('Stack is empty')

'''
The implementation of the stack is handled by the stack, the client does not need to know

The clien
'''