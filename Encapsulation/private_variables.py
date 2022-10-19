class PrivatePerson():
    def __init__(self, name, privateData):
        self.name = name
        self.__privateData = privateData

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name
        
'''
Python doesname mangling to self.__privateData => becomes self._PrivatePerson_privateData
Or set instance variables to a single underscore self._example but this is a convention and client code can access easy
'''