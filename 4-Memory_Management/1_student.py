# When a reference count of an object goes to zero, Python knows that the object can be safely deleted
# Right before destroying an object, Python calls a magic method of that object named __del__() to inform the object
# In any class, you can write your own version of the __del__() method
# In your version, you can include any code you want the object to execute before the object diappears forever
# Examples: your object may want to close a file, close a network connection
# When an object is deleted, Python checks to see if any of its instance variables refer to other objects
# If so, the reference count of those objects are also decremented
# If this results in another object's reference count going to zero, then that object is deleted as well


class Student():

    def __init__(self, name):
        self.name = name
        print('Creating Student object', self.name)

    def __del__(self):
        print('In the __del__ method for student:', self.name)




class Teacher():

    def __init__(self):
        print('Creating the Teacher object')
        self.oStudent1 = Student('Joe')
        self.oStudent2 = Student('Sue')
        self.oStudent3 = Student('Chris')

    def __del__(self):
        print('In the __del__ method for Teacher')


oTeacher = Teacher()                            ''' After starting up, the Teacher object has 3 instance variables that are student objects '''

# >>> Creating the Teacher object
# >>> Creating Student object Joe           
# >>> Creating Student object Sue
# >>> Creating Student object Chris

del oTeacher                                    

# >>> In the __del__ method for Teacher       
# >>> In the __del__ method for student: Joe  
# >>> In the __del__ method for student: Sue  
# >>> In the __del__ method for student: Chris

''' del now refers to the magic method created in oTeacher, that magic method in the oTeacher object is called.
When the Teacher object is deleted, Python sees that it contains three other objects (the three Student objects). So Python lowers the reference
count of each of those objects from 1 to 0. Once this happens, the __del__() method of the Student objects is called and each outputs a message. The memory
used by all three of the Student objects is then marked as garbage.

This is a demo but because Python keeps track of reference counts for all objects, you don't have tow worry about memory management in Python and rarely need
to include a __del__() method '''