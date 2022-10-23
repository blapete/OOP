import random
from abc import ABC, abstractmethod

# Color setup
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Shape(ABC):  #------------------------------------------------------------> inherits from ABC (abstract base class)
                                                                                # tells Python to prevent client code fro instantiating
    def __init__(self, window, shapeType, maxWidth, maxHeight):                 # a Shape object directly, trying to do do so will result as:
        self.window = window                                                    
        self.shapeType = shapeType
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
                                                                        # __init__() and getType() contain code shared by all subclasses of Shape
    def getType(self):
        return self.shapeType

    @abstractmethod
    def clickedInside(self, mousePoint):
        raise NotImplementedError

    @abstractmethod                                                     # the @abstractmethod decorator must be overwritten by all subclasses of Shape
    def getArea(self):                                                  # since these methods in this abstract class never run, the implementation here
        raise NotImplementedError                                       # consists only of raise NotImplementedError to further emphasize the method                         
                                                                        # doesn't do anything
    @abstractmethod
    def draw(self):
        raise NotImplementedError


'''
ORIGINAL CODE:
'''
# import random

# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# class Shape():

#     def __init__(self, window, shapeType, maxWidth, maxHeight):
#         self.window = window
#         self.shapeType = shapeType
#         self.color = random.choice((RED, GREEN, BLUE))
#         self.x = random.randrange(1, maxWidth - 100)
#         self.y = random.randrange(25, maxHeight - 100)

#     def getType(self):
#         return self.shapeType
'''
Shape base class has a potential bug:

A client could instantiate a generic Shape object which is too generic to have its own getArea() method
Further, all classes that inherit from the shape class must implement clickedInside(), getArea(), and draw()
This is solved using an abstract class and abstract method

Explained:
Often a base class cannot correctly implement an abstract method because it cannot know the detailed data it should operate on,
or it might not be possible to implement a general algorithm.
Instead all subclasses need to implement their own version of the abstract method.

Here (above) the Shape class is turned into an abstract class so no client code can instantiate a Shape object
Further, the Shape class should indicate that all its subclasses need to implement the clickedInside(), getArea(), and draw() methods.

Python does not have a keyword to designate a class or method as abstract.
The Python Standard Library contains the abc module (short for abstract base class) which is designed to help developers build abstract base classes and methods.

Put the @abstractmethod decorator before any methods that must be overwritten by all subclasses
'''