import math

# A vector is an ordered pair of x and y values that is often represented on a graph as a directed line segment

class Vector(): # represents two values as a vector, allows for math calculations using magic methods
 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oOther):  # +
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        return Vector(self.x + oOther.x, self.y + oOther.y)

    def __sub__(self, oOther):  # -
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther):  # *
        if isinstance(oOther, Vector):
            return Vector((self.x * oOther.x), (self.y * oOther.y))     # multiply two vectors
        elif isinstance(oOther, (int, float)):                          # multiply by a scalar
            return Vector((self.x * oOther), (self.y * oOther))
        else:
            raise TypeError('Second value must be a vector or scalar')

    def __abs__(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __eq__(self, oOther):  # ==
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        return (self.x == oOther.x) and (self.y == oOther.y)

    def __ne__(self, oOther):  # !=
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        return not (self == oOther)  # calls __eq__ method

    def __lt__(self, oOther):    # <
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        if abs(self) < abs(oOther):  # calls __abs__ method
            return True
        else:
            return False
        
    def __gt__(self, oOther):  # >
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        if abs(self) > abs(oOther):  # calls __abs__ method
            return True
        else:
            return False

    def __str__(self): # print out stringified values we want rather than memory address of the object
        return 'This vector has the value (' + str(self.x) + ', ' + str(self.y) + ')'

'''
The Vector class implements arithmetic and comparison operators as magic methods

Client code can use standard symbols for math and comparison between two Vector objects
'''


v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)

# Print Boolean or numeric values
print(v1 == v2)     # False
print(v1 == v3)     # True
print(abs(v1))      # 5
print(abs(v2))      # 2.8284
print(v1 < v2)      # False
print(v1 > v2)      # True
print()

# Print the vectors (calls the __str__() method)
print('Vector 1:', v1)                      # 3, 4
print('Vector 2:', v2)                      # 2, 2
print('Vector 1 + Vector 2:', v1 + v2)      # 5, 6
print('Vector 1 - Vector 2:', v1 - v2)      # 1, 2
print('Vector 1 times Vector 2:', v1 * v2)  # 6, 8
print('Vector 1 times 5:', v1 * 5)          # 15, 20

# https://docs.python.org/3/reference/datamodel.html