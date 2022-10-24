


class Point():

    def __init__(self, x, y):
        self.x = x                      
        self.y = y
        self.color = 'black'
        print(self.__dict__) # {'x': 1, 'y': 2, 'color': 'black'}



class PointWithSlots():

    # Define slots for only two instance variables
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'black'
        print(self.__slots__) # ['x', 'y']



oExample1 = Point(1,2)

oExample2 = PointWithSlots(3,4) # >>> AttributeError: 'PointWithSlots' object has no attribute 'color'




'''
When an object is instantiated Python must allocate space for the instance variables defined in the class.
By default Python does this using a dictionary with a special name: __dict__.


In order to allow for a dynamically changing number of instance variables, dictionaries are typically implemented with enough
empty space to represent some number of instance variabes (exact number is an internal detail of Python).


In the Point class, if hundreds of thousands or millions of objects were instantiated from it, it could cumulatively account for a large
amount of wasted memory space (RAM).


There is a special class variable __slots__ to define a list of variables up front to use for the instance variables.
Using slots is highly memory-efficient at the expense of a loss of dynamic instance variables.


Point uses __dict__ for instance variables, PointWithSlots uses __slots__, call self.dirs() to view this.
'''