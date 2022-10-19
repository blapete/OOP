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


# A decorator is a method that takes another method as an argument and extends the way the original method works
# Decorators can be functions that decorate functions or methods
# There is a set of built-in decorators that provide a compromise between direct access and the use of getters and setters in a class


# Property:
# An attribute of a class that appears to client code to be an instance variable, but instead causes a method to be called when it is accessed
# Using a property to (indirectly) access data in an object


class Student():

    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.grade = startingGrade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e)('New grade: ' + str(newGrade) + ', is an invalid type.')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError('New grade: ' + str(newGrade) + ', must be between 0 and 100.')
        self.__grade = newGrade


oStudent1 = Student('Joe Schmoe')
oStudent2 = Student('Jane Smith')

# Get the students' grades using the grade property
print(oStudent1.grade)
print(oStudent2.grade)
print()

# Set new values using the grade property
oStudent1.grade = 85
oStudent2.grade = 92

oStudent1.grade = 'abc'


print(oStudent1.grade)
print(oStudent2.grade)