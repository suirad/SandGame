from random import randint
from sand.stype import bit, water

SANDCOLOR = (238, 232, 170)

class Sand(bit.Bit):
    "The Sandiest sand"
    def __init__(self):
        self.color = SANDCOLOR
        self.move = False
    def clone(self):
        return Sand()
    def tick(self, coords, allpix):
        if self.move is True:
            self.move = False
            newcoords = (coords[0] + randint(-1, 1), coords[1] + 1)
        else:
            self.move = True
            newcoords = (coords[0], coords[1] + 1)
        return newcoords
    def interact(self, oldcoord, newcoord, pix, allpix):
        if isinstance(pix, water.Water):
            allpix[oldcoord] = pix
            allpix[newcoord] = self
        return False

