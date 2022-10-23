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

# Throws an error
#   def draw(self):
#       pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))