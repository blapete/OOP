import pygame
from pygame.locals import *
import sys


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


pygame.init()


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

ballImage = pygame.image.load('images/ball.png')


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    window.fill(BLACK)
    
    # draw ball
    window.blit(ballImage, (100, 200))    

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
Every time throught the loop the program draws the ball

The location of the upper left corner (pixel) of the image bounding rectangle at 100 across, 200 down

blit() is a very old reference to the words bit block transfer, here it means draw

On each iteration, every pixel in the window is set to black, then the ball is drawn over the background

In official documentation of pygame, every image including the application window is known as a surface
'''