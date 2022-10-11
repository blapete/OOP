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
       
# 3
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4

# 5
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 6 
while True:
    
    # 7
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    # 8
    oBall.update()  # tell the ball to update itself

   # 9
    window.fill(BLACK)
    
    # 10
    oBall.draw()   # tell the ball to draw itself


    # 11
    pygame.display.update()

    # 12
    clock.tick(FRAMES_PER_SECOND)


'''
Simplified main code
'''