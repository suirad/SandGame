from sand.stype import bit

STONECOLOR = (128, 128, 128)

class Stone(bit.Bit):
    "The Stoniest stone"
    def __init__(self):
        self.color = STONECOLOR
    def clone(self):
        return Stone()

