from maptile import *
from basezone import *
import random

class World(object):
    def __init__(self, seed=None):
        if (seed == None):
            random.seed()
        else:
            random.seed(seed)
        self.map = dict()
    def generateTile(self, x, y):
        newtile = MapTile(x,y, self)
        self.map[(x,y)] = newtile
        #TODO: Actual generation code
        sky = BaseZone(newtile, "test", "SKY")
        ground = BaseZone(newtile, "test2", "GROUND")
        sky.setBelow(ground)
        ground.setAbove(sky)
        newtile.addLevel("SKY", sky)
        newtile.addLevel("GROUND", ground)
    def getTile(self, x, y):
        return self.map[(x,y)]
