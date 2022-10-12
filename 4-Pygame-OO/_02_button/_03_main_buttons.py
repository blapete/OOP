import pygame
from pygame.locals import *
from _01_button import *
import sys


GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  


# 3 instances of te SimpleButton class
oButtonA = SimpleButton(window, (25, 30), 
                        'images/buttonAUp.png', 
                        'images/buttonADown.png')
oButtonB = SimpleButton(window, (150, 30),
                        'images/buttonBUp.png', 
                        'images/buttonBDown.png')
oButtonC = SimpleButton(window, (275, 30), 
                        'images/buttonCUp.png', 
                        'images/buttonCDown.png')


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButtonA.handleEvent(event):
            print('User clicked button A.')
        elif oButtonB.handleEvent(event):
            print('User clicked button B.')
        elif oButtonC.handleEvent(event):
            print('User clicked button C.')

    window.fill(GRAY)
    
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
Since there are three instances of the sampe SimpleButton class, the behavior of each button will be identical

A benefit of this approach is that any change to the code in the SimpleButton class will affect all buttons instantiated from the class
'''