import pygame
from pygame.locals import *

class SimpleButton():
    # State
    STATE_IDLE = 'idle'             # no click
    STATE_ARMED = 'armed'           # clicked, mouse over button
    STATE_DISARMED = 'disarmed'     # clicked, mouse away from button
        
    def __init__(self, window, xy, imageUp, imageDown):
        self.window = window
        self.xy = xy
        self.surfaceUp = pygame.image.load(imageUp)
        self.surfaceDown = pygame.image.load(imageDown)

        self.screenPosition = self.surfaceUp.get_rect() # Get the rect for checking
        self.screenPosition[0] = xy[0]
        self.screenPosition[1] = xy[1]

        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        eventPointInButtonRect = self.screenPosition.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE: # Idle
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED: # Armed
            if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True
            if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED: # Disarmed
            if eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        if self.state == SimpleButton.STATE_ARMED:          # Armed
            self.window.blit(self.surfaceDown, self.xy)
        else:                                               # Idle or Disarmed
            self.window.blit(self.surfaceUp, self.xy)


'''
When the main program detects any event, it calls the handleEvent() method

This method first checks that the event is one of MOUSEMOTION, MOUSEBUTTONUP, or MOUSEBUTTONDOWN

The handleEvent() method returns True when the user completes a mouse click by pressing down on the button, then later releasing on the same button

In all other cases handleEvent() returns False

The draw() method uses the state of the object's instance variable self.state to decide which image (up or down) to draw

This code uses a state machine approach
'''