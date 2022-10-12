import pygame
from pygame.locals import *


class SimpleText():

    def __init__(self, window, xy, textValue, textColor):
        pygame.font.init()
        self.window = window
        self.xy = xy
        self.font = pygame.font.SysFont(None, 30)
        self.textColor = textColor
        self.text = None                # self.setValue(textValue) force creation of initial text image
        self.setValue(textValue)        # initial text

    def setValue(self, newText):  

        if self.text == newText:        # optimization
            return 

        self.text = newText
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
    
        self.window.blit(self.textSurface, self.xy)


'''
1. 

The class hides all the details of pygame's rendering of text, the user of the class never needs to know what pygame-specific calls are needed to show text

2. 

Each SimpleText object remembers the window that it draws into, the location where the text should be placed, and the text color

These values only need to be specified once when that object is instantiated, typically before the main loop starts

3.

Each SimpleText object is also optimized to remember both the text that it was last told to draw and the image (self.textSurface) that is made from the current text

It only needs to render a new surface when the text changes

4.

To show multiple pieces of text in a window, just instantiate multiple SimpleText objects

This is a key concept of object-oriented programming
'''