from random import randint
from sand.stype import bit, water

FIREMAINCOLOR = (255, 0, 0)
FIREHIGHCOLOR = (255, 140, 0)
FIRELOWCOLOR = (255, 215, 0)

class Fire(bit.Bit):
    "Best fire"
    def __init__(self):
        self.move = False
        self.life = randint(30, 100)
        if self.life > 50:
            self.color = FIREMAINCOLOR
        elif self.life > 25:
            self.color = FIREHIGHCOLOR
        else:
            self.color = FIRELOWCOLOR
    def clone(self):
        return Fire()
    def tick(self, coords, allpix):
        self.life -= 1
        if self.life < 0:
            return (-1, -1)
        elif self.color is FIREMAINCOLOR and self.life < 50:
            self.color = FIREHIGHCOLOR
        elif self.color is FIREHIGHCOLOR and self.life < 25:
            self.color = FIRELOWCOLOR
        if self.move is True:
            self.move = False
            return (coords[0]+randint(-1, 1), coords[1]-1)
        else:
            self.move = True
            return (coords[0], coords[1]-1)
    def interact(self, oldcoord, newcoord, pix, allpix):
        if isinstance(pix, water.Water):
            self.life = 0
            return False
        else:
            self.life = 0
            return True
