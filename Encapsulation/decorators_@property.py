class Example():
    def __init__(self, startingValue):
        self._x = startingValue

    @property
    def x(self):            # decorated getter method
        return self._x

    @x.setter
    def x(self, value):     # decorated setter methed
        self._x = value

oExample = Example(10)
print(oExample.x)
oExample.x = 20

'''
- A decorator is a method that takes another method as an argument and extends the way the original method works
- Decorators can also be functions that decorate functions or methods
- There is a set of built-in decorators that provide a compromise between direct access and the use of getters and setters in a class

@<decorator>
def <someMethod>(self, <parameters>)

- Property:
- An attribute of a class that appears to client code to be an instance variable, but instead causes a method to be called when it is accessed
'''