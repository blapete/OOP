class Person():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary



oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

print(oPerson1.getSalary())
print(oPerson2.getSalary())

oPerson1.setSalary(100000)
oPerson2.setSalary(111111)

print(oPerson1.getSalary())
print(oPerson2.getSalary())


'''
The strict approach to encapsulation says that client code never accesses an instance variable directly.
If a class wants to allow client software to access the information held inside an object, the standard approach is to use getter and setter method in the class.

Getter:
A method that retrieves data from an object instantiated from a class.

Setter:
A method that assigns data itno an object instantiated from a class.

Getters and setters are designed to allow writers of client software to get data from and set data of an object without knowledge of the implementation of the class.
This specifically means not needing to know names of instance variables.
Using getters and setters enforces a layer of protection.
'''