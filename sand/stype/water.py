from random import randint
from sand.stype import bit, fire

WATERCOLOR = (0, 0, 255)

class Water(bit.Bit):
    "Wettest water"
    def __init__(self):
        self.color = WATERCOLOR
    def clone(self):
        return Water()
    def tick(self, coords, allpix):
        if allpix.get((coords[0], coords[1]+1)) is None:
            return (coords[0], coords[1]+1)
        return (coords[0] + randint(-3, 3), coords[1])

    def interact(self, oldcoord, newcoord, pix, allpix):
        if isinstance(pix, fire.Ember):
            return True
        return False

