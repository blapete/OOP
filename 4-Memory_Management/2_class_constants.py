''' Class variable constants '''



# With this technique, every object instantiated from SpaceShip has to take the time to load the image and takes up all the memory needed to represent a copy of the same image

class SpaceShip():

    def __init__(self, window,...)
        self.image = pygwidgets.Image(widnow, (0,0), 'images/ship.png')

# Have the class load the image once, and each SpaceShip object then uses the single image kept in the class like this

class SpaceShip():
    
    SPACE_SHIP_IMAGE = pyagme.image.load('images/ship.png')
    def __init__(self, window,...):
        self.image = pygwidgets.Image(window, (0,0), SpaceShip.SPACE_SHIP_IMAGE)

# This results in faster startup time and lower memory usage