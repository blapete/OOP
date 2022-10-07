# 1 packages
import pygame
from pygame.locals import *
import sys


# 2 constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# 3 initialize game world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

# 4 load assets images/sounds/etc.


# 5 variables
 

# 6 forever
while True:

    # 7 check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:          
            pygame.quit()  
            sys.exit()

    # 8 any "per frame" actions
    
    # 9 clear window
    window.fill(BLACK)
    
    # 10 draw window elements

    # 11 update display
    pygame.display.update()

    # 12 control game speed
    clock.tick(FRAMES_PER_SECOND) # make pygame wait