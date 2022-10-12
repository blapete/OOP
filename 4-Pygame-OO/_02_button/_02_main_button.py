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


# Instance of the SimpleButton class
oButton = SimpleButton(window, (150, 30),
                        'images/buttonUp.png',
                        'images/buttonDown.png')


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # give the event to the button
        if oButton.handleEvent(event):
            print('True returned, user has clicked the button.')

    # 9
    window.fill(GRAY)
    
    # 10
    oButton.draw()

    # 11
    pygame.display.update()

    # 12
    clock.tick(FRAMES_PER_SECOND)


'''
In the main loop, any time an event happens the handleEvent() method needs to be called to see if the user has clicked the button

The handleEvent() method tracks all of the user's actions on the button (pressing down, releasing, rolling off, rolling back on)
'''