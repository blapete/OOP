# packages
import pygame
from pygame.locals import *
import sys


# constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# initialize
pygame.init()


# build window/clock
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

# start the loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    window.fill(BLACK)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)