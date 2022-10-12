import pygame
from pygame.locals import *
import sys
import random
from _02_text_display import *
from _04_ball import *
from _05_button import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 
       

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (60, 20),'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), 'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if oRestartButton.handleEvent(event):
            frameCounter = 0  # clicked button, reset counter

    # 8
    oBall.update()
    frameCounter = frameCounter + 1  # increment each frame
    oFrameCountDisplay.setValue(str(frameCounter))
    # 8 end

    window.fill(BLACK)
    
    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
1. Check if the user pressed the restart button

2. Tell the ball to update its position

3. Increment the frame counter, then setValue() to show the new count of frames

4. Tell the ball, text fields, and restart button to draw themselves in that order
'''