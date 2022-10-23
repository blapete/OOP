import pygame
from shape import *

class Square(Shape): # inherits from Shape

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Square', maxWidth, maxHeight) # call init method of its superclass
        self.widthAndHeight = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight, self.widthAndHeight)

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
    
    def getArea(self):
        theArea = self.widthAndHeight * self.widthAndHeight
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeight))