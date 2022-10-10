import pygame
from pygame.locals import *
import pygwidgets
import sys


GRAY = (200, 200, 200)
WINDOW_WIDTH = 270
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  


barkSound = pygame.mixer.Sound('bark.wav')
meowSound = pygame.mixer.Sound('meow.wav')


buttonA = pygwidgets.TextButton(window, (20, 30), 'Bark')
buttonB = pygwidgets.TextButton(window, (150, 30), 'Meow')

counter = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass event to the button, see if has been clicked
        if  buttonA.handleEvent(event):
            print('User pressed the Bark button.  Program has run this many loops:', counter)
            barkSound.play()
        elif  buttonB.handleEvent(event):
            print('User pressed the Meow button.  Program has run this many loops:', counter)
            meowSound.play()

    # 8
    counter = counter + 1
    
    window.fill(GRAY)
    
    # 10
    buttonA.draw()
    buttonB.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
A simple GUI program with two buttons: Bark and Meow.

The user can click the buttons at any time, the program runs in a loop and constantly checks to see if either button has been clicked.

When the program receives a mouse down event, it remembers which button has been clicked and draws a depressed image of that button.

When the program receives a mouse up event, it remembers the new state and redraws that button with its original appearance, and then plays the appropriate sound.

Because the main loop runs so quickly, the user perceives that the sound plays immediately after the click the button.

Each time through the loop the program redraws both buttons with an image matching each button's current state.
'''