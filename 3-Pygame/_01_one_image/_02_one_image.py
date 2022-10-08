# packages (1)
import pygame
from pygame.locals import *
import sys


# game constants (2)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# initialize pygame (3)
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

# load assets (4)
ballImage = pygame.image.load('images/ball.png')


# infinity loop (6)
while True:

    # 7 Check events (7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # Clear window (9)
    window.fill(BLACK)
    
    # Draw window (10)
    window.blit(ballImage, (100, 200))    

    # Update window (11)
    pygame.display.update()

    # Control loop speed (12)
    clock.tick(FRAMES_PER_SECOND)


'''
Every time throught the loop the program draws the ball

The location of the upper left corner (pixel) of the image bounding rectangle at 100 across, 200 down

blit() is a very old reference to the words bit block transfer, here it means draw

On each iteration, every pixel in the window is set to black, then the ball is drawn over the background

In official documentation of pygame, every image including the application window is known as a surface
'''