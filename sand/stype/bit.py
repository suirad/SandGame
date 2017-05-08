

class Bit(object):
    """
    Inheritable Sand bit object
    Init needs to implement a member 'color' which is an rgb(a) tuple
    For performance, I recommend referencing a global color object,
        so that its not duplicated for each pixel
    """
    def clone(self):
        "Needs to just return another object of the same class when implemented"
        pass
    def tick(self, coords, allpix):
        """
        This is called every game tick, for every pixel. Return value should
            be a tuple of the new location to move this pixel to, or the same
            coord if nothing should happen after that. Return (-1, -1) to be
            removed
        """
        return coords
    def interact(self, oldcoord, newcoord, pix, allpix):
        """
        This is called if tick returns a location other than its given coord.
        Coord will be the new coord and pix will be the pixel in the way.
        Return value needs to be True if this pixel replaces the old, or false if not.
        """
        return False

