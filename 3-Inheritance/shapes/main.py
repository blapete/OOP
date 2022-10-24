import pygame
import sys
from pygame.locals import *
from Square import *
from Circle import *
from Triangle import *
import pygwidgets


WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 10


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()


shapesList = []
shapeClassesTuple = (Square, Circle, Triangle)

for i in range(0, N_SHAPES):                                                                # The (this) main code, as a client of these classes, implements Square, Circle, and Triangle
    randomlyChosenClass = random.choice(shapeClassesTuple)                                  # objects without having to worry about the implementation of those classes.
    oShape = randomlyChosenClass(window, WINDOW_WIDTH, WINDOW_HEIGHT)                       
    shapesList.append(oShape)                                                               # It doesn't need to know that each is subclassed from a common Shape class.

oStatusLine = pygwidgets.DisplayText(window, (4, 4), 'Click on shapes', fontSize=28)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oShape in shapesList:
                if oShape.clickedInside(event.pos):
                    thisArea = oShape.getArea()
                    thisType = oShape.getType()
                    newText = 'Clicked on a ' + thisType + ' whose area is ' + str(thisArea)
                    oStatusLine.setValue(newText)

    window.fill(WHITE)

    # tell each shape to draw itself
    for oShape in shapesList:
        oShape.draw()

    oStatusLine.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)