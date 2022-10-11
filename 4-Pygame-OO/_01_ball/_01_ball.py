import pygame
from pygame.locals import *
import random


class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, to draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('images/ball.png')
        # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        # random starting position 
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # random speed between -4 and 4, but not zero
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4] 
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # check for hitting a wall
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # update ball location, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


'''
In the previous example (_05_location_animation), the data for the ball and the code to manipulate the ball are intertwined


A more modular approach is to split the code into a Ball class and a main program that instantiates a Ball object and makes calls to its methods

To do this, extract all code relating to the ball from the main program and move it into a separate Ball class.
'''