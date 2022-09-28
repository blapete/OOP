# Dimmer switch for example


class DimmerSwitch():

    def __init__(self, label):
        self.label = label
        self.switchIsOn = False
        self.brightness = 0
        
    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1


    def show(self):
        print('Label:', self.label)
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)


# Create 3 DimmerSwitch objects:

oDimmer1 = DimmerSwitch('Dimmer1')
print(type(oDimmer1))
print(oDimmer1)
print()

oDimmer2 = DimmerSwitch('Dimmer2')
print(type(oDimmer2))
print(oDimmer2)
print()

oDimmer3 = DimmerSwitch('Dimmer3')
print(type(oDimmer3))
print(oDimmer3)
print()

'''
Output:
<class '__main__.DimmerSwitch'>
<__main__.DimmerSwitch object at 0x01D46148>

<class '__main__.DimmerSwitch'>
<__main__.DimmerSwitch object at 0x01D46238>

<class '__main__.DimmerSwitch'>
<__main__.DimmerSwitch object at 0x01D46298>


The first line in each grouping tells the data type
Instead of built-in types like integer or float, all three objects are of the programmer-defined DimmerSwitch type
The __main__ indicats that the DimmerSwitch code was found inside this python file, not imported from another file

The second line in each grouping conatins a string, which represents a location memory of the computer


All DimmerSwitch objects report the same type: class DimmerSwitch
The important concept is that the objects all refer to the code of the same class, which only exists in one place


Classes can contain hundreds or thousands of lines of code, no object actually gets a copy of the class's code
Having one copy of the code is very important and keeps the size of OOP programs small
Instantiating an object from a class is memory-efficient


The code of a class only exists in one place
When creating a new instance of an object, Python allocates memory to represent the INSTANCE VARABLES defined in that class
No duplicates of the class's code are made
'''

print('oDimmer1 variables:', vars(oDimmer1))
print()

'''
Internally, all instance variables of an object are kept as name value pairs in a Python dictionary
You can inspect all the instance variables in an object by calling the built-in vars() functoin on any object
'''