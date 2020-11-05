import random

# The class of the dice, by default it got 6 sides and the side thats turns up is random
class Die:
    sides = 6
    sideUp = random.randint(1,6)
    dieColor = "#ffffff"
    dotColor = "#000000"

    # The constructor of the dice
    """
    posX = X-coordinate for bottom-left corner of the dice
    posY = Y-coordinate for bottom-left corner of the dice
    size = lengt of the sides
    """
    def __init__(self, posX, posY, size):
        self.posX = posX
        self.posY = posY
        self.size = size

    # Method for changing the colors of the dice
    def setColor(self, dieColor, dotColor):
        self.dieColor = dieColor
        self.dotColor = dotColor

    # Method for rolling the dice. Sets the side up to a new random number, then returns it
    def roll(self):
        self.sideUp = random.randint(1,6)
        return self.sideUp



