# 1
import pygame
from pygame.locals import *
import sys
import random
from _01_ball import *  # bring in the Ball class code

# 2
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 
N_BALLS = 3

# 3
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4

# 5
ballList = []
for oBall in range(0, N_BALLS):
    # each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)

# 6 
while True:
    
    # 7
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    # 8
    for oBall in ballList:
        oBall.update() # tell each ball to update itself

   # 9
    window.fill(BLACK)
    
    # 10
    for oBall in ballList:
        oBall.draw() # tell each ball to draw itself

    # 11
    pygame.display.update()

    # 12
    clock.tick(FRAMES_PER_SECOND)


'''
Using this OO aproach, no changes were made to the Ball class

Only the main program was changed to manage a list of Ball objects instead of a single Ball object

Each frame iterates through the list of Ball objects, telling each one to update its location, then iterate again to tell each one to draw itself
'''