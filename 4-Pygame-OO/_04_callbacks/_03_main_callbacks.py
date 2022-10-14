import pygame
from pygame.locals import *
from _04_button import *
import sys


GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30


# Callback function example
def exampleFunction():
    print('User pressed Button B, called exampleFunction')

# Callback method example
class Example():
    def __init__(self):
        pass

    def exampleMethod(self):
        print('User pressed Button C, called exampleMethod of the Example object')


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  


# 5
oExample = Example()

oButtonA = SimpleButton(window, (25, 30), 'images/buttonAUp.png', 'images/buttonADown.png')                                          # No call back
oButtonB = SimpleButton(window, (150, 30), 'images/buttonBUp.png', 'images/buttonBDown.png', callBack=exampleFunction)               # Specifying a function to call back
oButtonC = SimpleButton(window, (275, 30), 'images/buttonCUp.png', 'images/buttonCDown.png', callBack=oExample.exampleMethod)        # Specifying method to call back
counter = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # give the event to the button
        if oButtonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        # oButtonB and oButtonC have callbacks,
        # no need to check result of these calls
        oButtonB.handleEvent(event)

        oButtonC.handleEvent(event)

    counter = counter + 1
    
    window.fill(GRAY)
    
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
The main loop checks for the user clicking on any of the three buttons by calling the handleEvent() method of each button

Since oButtonA has no callback, the code checks if the returned value is True and, if, so, perform an action

When oButtonB is clicked, the exampleFunction() function will be called and will print its message

When oButtonC is clicked, the exampleMethod() method of the oExample object will be called and will print its message
'''