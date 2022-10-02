# State and behavior - procedural


def turnOn():
    global switchIsOn
    switchIsOn = True

def turnOff():
    global switchIsOn
    switchIsOn = False
    

# Main
switchIsOn = False


# Test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)


'''
Model real-world object in code:

What data will represent that objects attributes? What operations can it perform?

These two concepts are referred to as an object's state and behavior

The state is the data that the object remembers
The behaviors are the actions that the objects can do
'''