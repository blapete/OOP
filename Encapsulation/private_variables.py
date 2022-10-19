class PrivatePerson():
    def __init__(self, name, privateData):
        self.name = name
        self.__privateData = privateData

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name

'''
- Python does name mangling and prepends a double underscore name with an underscore and name of the class
- self.__privateData becomes self._PrivatePerson__privateData
- It is a deterrent but not a guarantee client software can't access it

- Another way to mark it as one that should never be accessed
    self._name
    def _internalMethod(self):
- Naming like this is inteded to represent private data, client software should never attempt to access them directly
'''