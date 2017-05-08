from sand.stype import bit

WOODCOLOR = (139, 69, 19)

class Wood(bit.Bit):
    "Some Flamable wood"
    def __init__(self):
        self.color = WOODCOLOR
    def clone(self):
        return Wood()

