from random import randint
from sand.stype import bit

WATERCOLOR = (0, 0, 255)

class Water(bit.Bit):
    "Wettest water"
    def __init__(self):
        self.color = WATERCOLOR
    def clone(self):
        return Water()
    def tick(self, coords, allpix):
        if allpix.get((coords[0], coords[1]+1)) is None:
            newpos = (coords[0], coords[1]+1)
            return newpos
        newpos = (coords[0] + randint(-1, 1), coords[1])
        if allpix.get(newpos) is None:
            return newpos
        elif allpix.get((newpos[0], newpos[1]+1)) is None:
            return (newpos[0], newpos[1]+1)
        return coords

    def interact(self, oldcoord, newcoord, pix, allpix):
        return False

