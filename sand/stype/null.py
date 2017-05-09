
from random import randint
from sand.stype import bit

NULLCOLOR = (128, 128, 128)
DIE = (-1, -1)

class Null(bit.Bit):
    "Eats other types"
    def __init__(self):
        self.color = NULLCOLOR
        self.delay = randint(60, 100)
    def clone(self):
        return Null()
    def tick(self, coords, allpix):
        if self.delay > 0: self.delay -= 1
        for coord in [
            (coords[0]-1, coords[1]-1), (coords[0], coords[1]-1),
            (coords[0]+1, coords[1]-1), (coords[0]-1, coords[1]),
            (coords[0]+1, coords[1]), (coords[0]-1, coords[1]+1),
            (coords[0], coords[1]+1), (coords[0]+1, coords[1]+1)
        ]:
            if allpix.get(coord) is not None:
                allpix[coord] = Null()
        return DIE



