import pygame
from pygame.locals import *
import sys
import random


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

ballImage = pygame.image.load('images/ball.png')


ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
 

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

    # Update rectangle of the ball, using the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed
    # 8 end

    window.fill(BLACK)
    
    window.blit(ballImage, ballRect)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
This code shows how to use and manipulate attributes of a rect object, neither better or worse than using separate variables

The ball image is loaded and the get_rect() method is called to get the bounding ractangle of the image

The method returns a rect object which then is stored in the ballRect variable

ballRect.width and ballRect.height are used to get to get the width and height of the ball image

Getting the values from the image this way makes the code much more adaptable bevause it will adapt to a graphic of any size

The code uses attributes of the rectangle to check if any part of the ball's rectangle crosses a window edge

Rather than update individual x- and y-coordinate variables, the left and top of ballRect are updated

The second argument blit() can be either an (x,y) tuple or a rect, it uses the left and top position in the rect as the x- and y-cordinates
'''