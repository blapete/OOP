import pygame
from shape import *

class Rectangle(Shape): # inherits from Shape

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Rectangle', maxWidth, maxHeight) # call init method of its superclass
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def getArea(self):
        theArea = self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

''' If commented out, Python throws error >>> TypeError: Can't instantiate abstract class Rectangle with abstract method draw 
    This means the code cannot instantiate a Rectangle object becasue it does not have a draw() method in the Rectangle class  '''

#   def draw(self):
#       pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))