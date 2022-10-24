import random


# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Shape():  # the base class

    def __init__(self, window, shapeType, maxWidth, maxHeight):
        self.window = window
        self.shapeType = shapeType
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

    def getType(self):  # the three sublasses circle, square, and triangle all inherit this method
        return self.shapeType

'''
The __init__() method emembers the data passed in in instance variables, then randomly chooses a color and starting location self.x and self.y

The three subclasses called will call the init method of the Shape class and pass in a string that identifies its type and the size of the window
'''