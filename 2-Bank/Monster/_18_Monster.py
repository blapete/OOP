# Monster game


import random


class Monster():

    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows  # save away
        self.nCols = nCols  # save away
        self.myRow = random.randrange(self.nRows) #chooses a random row
        self.myCol = random.randrange(self.nCols) #chooses a random col
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed) + 1 # chooses an X speed
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed) + 1 # chooses a Y speed
        # Set other instance variables like health, power, etc.

    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) %  self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols
    

N_MONSTERS = 20
N_ROWS = 100   # could be any size
N_COLS = 200   # could be any size
MAX_SPEED = 4


monsterList = []  # start with an empty list
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)  # create a Monster
    monsterList.append(oMonster)  # add Monster to our list


# Later, when playing the game
for oMonster in monsterList:
    oMonster.move()


'''
The loop instantiates 20 Monsters

Each Monster knows its own starting location in the gris and its individual speed

The list of objects is created

Later in the program, a loop can be used to call the same method on each object in the list

for objectVariable in objectVariablesList:
    objectVariable.someMethod()

Example:

for oMonster in monsterList:
    oMonster.move()

Since each Monster object remembers its location and speed, in the move() method each Monster can move to and remember its new location

The technqiue of building a list of objects and calling the same method of all the objects is a standard approach

Very useful when dealing with a collection of similar objects
'''