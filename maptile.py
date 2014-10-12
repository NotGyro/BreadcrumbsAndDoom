#A container for the contexts where actual gameplay takes place.
class MapTile(object):
        def __init__(self, x, y, world):
                self.x = x
                self.y = y
                self.world = world
                self.levels = dict()
        def addLevel(self, lev):
                self.levels[lev.getLevel()] = lev
        def getLevel(self, name):
                if name in self.levels:
                        return self.levels[name]
                else:
                        return None
        def getWorld(self):
                return self.world
