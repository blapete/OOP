''' Class variable for counting '''



# In the Sample class, nObjects is a class variabe because it is defined in the class scope, typically between the class statement and the first def statement

class Sample():

    nObjects = 0
    def __init__(self, name):
        self.name = name
        Sample.nObjects = Sample.nObjects + 1

    def howManyObjects(self):
        print('There are', Sample.nObjects, 'Sample objects')

    def __del__(self):
        Sample.nObjects = Sample.nObjects - 1


oSample1 = Sample('A')
oSample2 = Sample('B')
oSample3 = Sample('C')
oSample4 = Sample('D')

del oSample3


oSample1.howManyObjects()

# >>> There are 3 Sample objects

print(Sample.nObjects)


