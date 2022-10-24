import random
from abc import ABC, abstractmethod


# set up the colors
RED = (255, 0, 0)                                                               # The point of using an abstract Shape class is so no client code 
GREEN = (0, 255, 0)                                                             # can instantiate a Shape object. 
BLUE = (0, 0, 255)


class Shape(ABC):  # the base class-------------------------------------------> inherits from ABC (abstract base class)
                                                                                # This tells Python to prevent client code from instantiating
    def __init__(self, window, shapeType, maxWidth, maxHeight):                 # a Shape object directly.
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

    @abstractmethod                                                             # The decorator indicates these methods must be overwritten by all subclasses of Shape.
    def getArea(self):                                                          # Since these methods in this abstract class never run, the implementation here consists only 
        raise NotImplementedError                                               # of raise NotImplementedError to further emphasize the method doesn't do anything.                      
                                                                        
    @abstractmethod
    def draw(self):
        raise NotImplementedError


'''
In the original code from the shapes folder:
The Shape base class has a potential bug


A client could instantiate a generic Shape object which is too generic to have its own getArea() method, and all classes that inherit from the Shape class must implement clickedInside(), getArea(), and draw() =>
This is solved using an abstract class and abstract method.


Sometimes a base class cannot correctly implement an abstract method because it cannot know the detailed data it should operate on, or it might not be possible to implement a general algorithm =>
Instead all subclasses need to implement their own version of the abstract method.


In this folder shapes_abstract, the Shape class is turned into an abstract class so no client code can instantiate a Shape object =>
The Shape class should indicate that all its subclasses need to implement the clickedInside(), getArea(), and draw() methods.


Python does not have a keyword to designate a class or method as abstract.
The Python Standard Library contains the abc module (short for abstract base class) which is designed to help developers build abstract base classes and methods.


Put the @abstractmethod decorator before any methods that must be overwritten by all subclasses.
If the decorator is commented out, the code runs fine if each shape has all the required methods.
If the decorator is commented out, and a shape is missing one of the required method (draw() for example), the code immediately throws a NotImplementedError because the draw() method is called from the original format from the base Shape class that was inherited by one of the subclasses.
If the decorator is there, the code immediately throws an error as >>> TypeError: Can't instantiate abstract class Rectangle with abstract method draw, this shows that an abstract method was called, which cannot be called and acts as a safeguard.
''