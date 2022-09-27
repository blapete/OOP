# Dimmer switch class


class DimmerSwitch():
    # State
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
        
    # Behaviors
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

    # Show current value of the instance variables
    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)


# Main
oDimmer = DimmerSwitch() 
oDimmer.turnOn() # on
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff() # off
oDimmer.show()
oDimmer.turnOn() # on
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()


'''
Instance variables maintain their values between calls to methods of an object
The self.brightness instance variable is incremented by 1 for each call to oDimmer.raiseLevel()
'''