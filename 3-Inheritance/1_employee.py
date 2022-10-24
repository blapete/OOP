class Employee():

    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):  # getter
        return self.name

    def getTitle(self): # getter
        return self.title

    def payPerYear(self):
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay


'''
Manager subclass that inherits from Employee
Only needs to contain code that is different from employee class
Inherits all the code from Employee
'''
class Manager(Employee):

    def __init__(self, name, title, salary, reportsList=None):
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportsList = reportsList
        super().__init__(name, title)   #------------------------------------------------> SUPER(), tells Python figure out which class is the base class (superclass)
                                                                                           # and to call that class's __init__() method, adjusts arguments to include self
    def getReports(self):   # getter                                                       # as the first argument in the call => Employee.__init__(self, name, title), using this                 
        return self.reportsList                                                            # function call would actually work as well, super() is a shortcut
                                                                                           # Older versions of python required the code to be written:
    def payPerYear(self, giveBonus=False):   # same method as Employee                     # super(Employee, self).__init__(name, salary)
        pay = self.salary                    # this functionality will override            # super() is safer in case you change name of the base class
        if giveBonus:                                                       #|
            pay = pay + (.10 * self.salary)                                 #|
            print(self.name, 'gets a bonus for good work')                  #|
        return pay                                                           #-----> overriding method must have exact same name but can have diff parameters

    def addEmployee(self, oEmployeeToAdd):
        self.reportsList.append(oEmployeeToAdd)

    def removeEmployee(self, oEmployeeToRemove):
        self.reportsList.remove(oEmployeeToRemove)


oEmployee1 = Employee('Joe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris', 'Cashier', 14)
oManager = Manager('Sue Jones', 'Pizza Restaurant Manager', 55000, [oEmployee1, oEmployee2])


print('Employee name:', oEmployee1.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee1.payPerYear()))
print('Employee name:', oEmployee2.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee2.payPerYear()))
print()

managerName = oManager.getName()
print('Manager name:', managerName)

print('Manager salary:', '{:,.2f}'.format(oManager.payPerYear(True)))
print(managerName, '(' + oManager.getTitle() + ')', 'direct reports:')
reportsList = oManager.getReports()
for oEmployee in reportsList:
    print('   ', oEmployee.getName(),
            '(' + oEmployee.getTitle() + ')')


print()
print('Employee 1 instance vars: ', oEmployee1.__dict__.keys())
print('Employee 2 instance vars: ', oEmployee2.__dict__.keys())
print('Manager instance vars: ', oManager.__dict__.keys())


'''
Adhering to the principle of coding by difference:
The __init__() method starts by initializing anything the __init__() method of the Employee class doesn't do
'''