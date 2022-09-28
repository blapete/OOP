# Dimmer switch class, 2 instances


class DimmerSwitch():
    def __init__(self):
        self.isOn = False
        self.brightness = 0
        
    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # For debugging
    def showState(self):
        print('Switch is on?', self.isOn)
        print('Brightness is:', self.brightness)   


# Main
oDimmer1 = DimmerSwitch( )
oDimmer2 = DimmerSwitch( )

print(type(oDimmer1))

oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

oDimmer1.showState()
oDimmer2.showState()