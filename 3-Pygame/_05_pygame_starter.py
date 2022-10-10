# 1 packages
import pygame
from pygame.locals import *
import sys


# 2 constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# 3 initialize game world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 

# 4 load assets images/sounds/etc.


# 5 variables
 

# 6 forever
while True:

    # 7 check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:          
            pygame.quit()  
            sys.exit()

    # 8 any "per frame" actions
    
    # 9 clear window before drawing it again
    window.fill(BLACK)
    
    # 10 draw all window elements

    # 11 update window
    pygame.display.update()

    # 12 control game speed
    clock.tick(FRAMES_PER_SECOND) # make pygame wait


'''
1. 
Import the pygame package and some constants defined inside pygame
Import the sys package which is used to quit the game

2.
Define constants 
- RGB of the background color
- Width and height of the window in pixels
- Refresh rate for the program, maximum # of times the program will loop per second (redraw the window)
- If the amount of work done in the loop is excessive, the program might run slower than this value but it will never run faster

3. 
Initialize the pygame environment
pygame.display.set_mode() creates a window object - the dimensions are passed into this function
pygame.time.Clock() creates a clock object - used at the bottom of the main loop to maintain maximum frame rate

4.
Code here to load external images, sounds, and so on from the disk

5.
Initialize any variables that the program will use

6.
While True infinite loop
Think of each iteration through the main loop as one frame in an animation

7.
Check for and handle events
pygame.event.get() gets a list of the events that happened since the last time loop
Iterate through list, each event is an object and has a type
If no event has happeed this code is skipped
Commonly called the event loop

8.
Code here that needs to run in every frame
This could involve moving things in the window or checking for collisions between elements

9.
Clear the window
On each iteration through the main loop the program must redraw the window, must be cleared first
The simplest approach is to fill the background with a color
window.fill()

10.
Draw all window elements
Things are drawn in the order they appear in the code, in layers from backmost to frontmost
If there are two partially overlapping circles A & B, and A is drawn first, then A will appear behind B
This is a natural mapping equivalent to the layers in graphics programs such as Photoshop

11.
Update the window
Pygame does the drawing from 8, 9, & 10 in an off-screen buffer
This tells the program to take the contents in the off-screen buffer and put them in the real window
pygame.display.update()


12.
Code here to make pygame wait until a given amount of time has elapsed 
This makes the frames of the program run at the frame rate that was specified, ensures consistency
clock.tick()
'''