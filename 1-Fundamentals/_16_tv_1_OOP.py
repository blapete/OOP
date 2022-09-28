# TV class


class TV():

    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]  
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM // 2
        
    def power(self):
        self.isOn = not self.isOn   # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1    # wrap around to the top channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if newChannel is not in the list, don't do anything

    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')


# Main
oTV = TV()  # create a TV object


oTV.power()
oTV.showInfo()


oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()


oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()


oTV.volumeDown()
oTV.mute()
oTV.showInfo()


oTV.setChannel(11)
oTV.setChannel(99)
oTV.mute()
oTV.showInfo()


'''
When calling a method:
<object>.<method>(<any arguments>)

Python takes the object you specify in the call and rearranges it to become the first argument

Any values in the parentheses of the method call are considered subsequent arguments after self

Passing the object as the first argument allows the method to run with the state of the object (instance variable values)
'''