import pygame
from pygame.locals import *

class SimpleButton():
    
    # State
    STATE_IDLE = 'idle'             # no click
    STATE_ARMED = 'armed'           # clicked, mouse over button
    STATE_DISARMED = 'disarmed'     # clicked, mouse away from button
        
    def __init__(self, window, xy, imageUp, imageDown, callBack=None):
        self.window = window
        self.xy = xy
        self.surfaceUp = pygame.image.load(imageUp)
        self.surfaceDown = pygame.image.load(imageDown)
        self.callBack = callBack

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
                # If a callback was specified, call it back
                if self.callBack != None:
                    self.callBack()
                return True  # clicked
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