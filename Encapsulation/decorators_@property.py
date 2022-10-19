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
# >>> 10
oExample.x = 20



# ---------------------------------------------------------------------------------------



class Student():

    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.grade = startingGrade # store the starting grade into property grade, validates input

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
print(oStudent1.grade)
print(oStudent2.grade)
print()
# >>> 0
# >>> 0
oStudent1.grade = 85
oStudent2.grade = 92
print(oStudent1.grade)
print(oStudent2.grade)
# >>> 85
# >>> 92