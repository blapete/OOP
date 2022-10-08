import pygame
from pygame.locals import *
import sys
import random


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 5


# initialize pygame
pygame.init()


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

# load assets
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.jpg')
 

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

          
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX = ballX - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ballY = ballY - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY = ballY + N_PIXELS_TO_MOVE


    # Check ball colliding with target
    ballRect = pygame.Rect(ballX, ballY,
                                       BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')
        
    # Clear window
    window.fill(BLACK)
    
    # Draw window
    window.blit(targetImage, (TARGET_X, TARGET_Y))  # draw target
    window.blit(ballImage, (ballX, ballY))          # draw ball 

    # Update window
    pygame.display.update()

    # Control loop speed
    clock.tick(FRAMES_PER_SECOND)


'''
Added a test for a key press in the event loop

Check for an event of type pygame.KEYDOWN

If a key down event is detected, the code checks which key was pressed

Each key has an associated constant in pygame, check if the user has pressed the left, up, down, or right arrow

For each key press, the value of the ball's x or y-coordinate is modified appropriately by a small number of pixels

Next a pygame rect object is created for the ball

Check if the two rectangles are overlapping:

<booleanVariable> = <rect1>.colliderect(<rect2>)

If they overlap, "Ball is touching the target" prints to the shell window

The target is drawn first so that when the two overlap, the ball appears over the target
'''