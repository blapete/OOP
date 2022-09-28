# Light switch class


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
oLightSwitch = LightSwitch()  # create a LightSwitch object

# Calls to methods
oLightSwitch.show() # call the show method of oLightSwitch
oLightSwitch.turnOn() # call the turnOn method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOff() # call the turnOff method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()