import pygame
from pygame.locals import *
import sys


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)
PURPLE = (255, 0, 255)


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    window.fill(GRAY)
    
    # 10
    # Draw a box
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)  # top
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)  # left
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)  # right
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)  # bottom
    # Draw an X in the box
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)
    
    # Draw a filled circle and an empty circle
    pygame.draw.circle(window, GREEN, (250, 50), 30, 0) # filled
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2) # 2 pixel edge

    # Draw a filled rectangle and an empty rectangle
    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0) # filled
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1) # 1 pixel edge
        
    # Draw a filled ellipse and an empty ellipse
    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0) # filled
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2) # 2 pixel edge

    # Draw a six-sided polygon
    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350), 
                                                            (410, 410), (350, 470),
                                                            (240, 470), (170, 410)))

    # Draw an arc
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)
    
    # Draw anti-aliased lines: a single line, then a list of points
    pygame.draw.aaline(window, RED, (500, 400),  (540, 470), 1)
    pygame.draw.aalines(window, BLUE, True, 
                                  ((580, 400), (587, 450),
                                   (595, 460), (600, 444)), 1)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
Drawing occurs in section 10

The code make calls to pygame's drawing functions to draw the primitives
'''