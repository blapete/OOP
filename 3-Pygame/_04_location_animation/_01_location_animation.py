import pygame
from pygame.locals import *
import sys
import random


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

ballImage = pygame.image.load('images/ball.png')


MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
 

while True:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 start
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed  # reverse X direction

    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

    # Update ball location, using the speed in two directions
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed
    # 8 end

    window.fill(BLACK)
    
    window.blit(ballImage, (ballX, ballY))

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


'''
The location of the image changes slightly in every frame

If the result of that movement would place any part of the image outside one of the window boundaries, the relevant coordinate reverses

xSpeed and ySpeed determine how far and in what direction the image should move in each frame

In this code the image will start by moving 3 pixels to the right (the positive x direction) and three pixels down (the positive y drection)

#8 per frame code:

The x- and y- coordinates handled separately

If the x-coordinate of the ball is less than zero (past the left edge) or past the MAX_WIDTH pixel (past the right edge), the sign reverses

This means the ball will start moving in the opposite x direction

The same condition is checked for the y with 0 and MAX_HEIGHT

The position of the ball updates by adding the xSpeed to the ballX coordinate and ySpeed to the ballY coordinate

The ball will have a new location on both axes

Since the values of ballX and ballY update in every frame, the ball appears to animate smoothly
'''