# Light switch class, 2 instances


class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
         self.switchIsOn = True

    def turnOff(self):
         self.switchIsOn = False

    # For testing
    def show(self):
        print(self.switchIsOn)
    

# Main
oLightSwitch1 = LightSwitch()  # create a LightSwitch object
oLightSwitch2 = LightSwitch()  # create another LightSwitch object


oLightSwitch1.show()
oLightSwitch2.show()

oLightSwitch1.turnOn() # Turn switch 1 on only

oLightSwitch1.show()
oLightSwitch2.show()