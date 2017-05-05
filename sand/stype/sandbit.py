from random import randint
from sand.stype import bit

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
        if allpix.get(newcoords) is None:
            return newcoords
        else:
            return coords
    def interact(self, coord, pix, allpix):
        return False

