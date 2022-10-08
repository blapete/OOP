import pygame
from pygame.locals import *
import sys
import random


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
# Ensure ball always appears fully in window
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT


pygame.init()


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

# load assets
ballImage = pygame.image.load('images/ball.png')


ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
 

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:    
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    window.fill(BLACK)
    
    window.blit(ballImage, (ballX, ballY))    

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
pygame.Rect() creates a rectangle

Defining a rectangle requires four parameters

<rectObject> = pygame.Rect(<x>, <y>, <width>, <height>)

A mouse up event is typically used to signal activation

This event is signaled by a new event.type value of pygame.MOUSEBUTTONUP

When the event occurs, the program checks to see if the location of the click was inside the current rectangle of the ball

When pygame detects that an event has happened, it builds an event object containing a lot of data

The (x,y) position of the click is retreived using event.pos, which provides two tuples of values

To separate the x- and y-coordinates the tuple can be unpacked:

mouseX, mouseY = event.pos

Check to see if the event happened inside the rectangle of the ball:

collidepoint()

<booleanVariable> = <someRectangle>.collidepoint(<someXYLocation>)

The method returns a Boolean True if the given point is inside the rectangle
'''