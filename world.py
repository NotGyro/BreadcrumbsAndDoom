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

        #Temporary vanity code for shits and giggles starts here:
        
        sky = None
        ground = None
        underground = None

        space = BaseZone(newtile, "Space", "SPACE", "Outer Fucking Space")
        
        skn = random.randrange(13)
        if skn < 6:        
            sky = BaseZone(newtile, "Sky", "SKY", "the sky")
        elif skn < 8:
            sky = BaseZone(newtile, "Clouds", "SKY", "some clouds")
        elif skn < 10:
            sky = BaseZone(newtile, "Rainclouds", "SKY", "a storm")
        else:
            sky = BaseZone(newtile, "Updraft", "SKY", "an updraft")
            if skn == 11:
                high = BaseZone(newtile, "High Updraft", "HUP", "the stratosphere")
                high.setBelow(sky)
                sky.setAbove(high)
                newtile.addLevel(high)

                space.setBelow(high)
                high.setAbove(space)

        hell = BaseZone(newtile, "Hell", "HELL")
        hpn = random.randrange(40)
        
        gn = random.randrange(10)
        ugn = random.randrange(5)
        if gn == 0:        
            ground = BaseZone(newtile, "City", "GROUND", "a city")
            if ugn >= 4:
                underground = BaseZone(newtile, "Metro", "UNDERGROUND", "subway tunnels")
                newtile.addLevel(underground)
            elif ugn >= 3:
                underground = BaseZone(newtile, "Metro", "UNDERGROUND", "a subway station")
                ground.setBelow(underground)
                underground.setAbove(ground)
                newtile.addLevel(underground)
            if (ugn >= 3) and (hpn == 0):
                #Hell tunnel time.
                underground.setBelow(hell)
                hell.setAbove(underground)
        elif gn < 5:        
            ground = BaseZone(newtile, "Forest", "GROUND", "a forest")
            if ugn >= 2:
                underground = BaseZone(newtile, "Cave", "UNDERGROUND", "a cave")
                ground.setBelow(underground)
                underground.setAbove(ground)
                newtile.addLevel(underground)
            if (ugn >= 3) and (hpn == 0):
                #Hell tunnel time.
                underground.setBelow(hell)
                hell.setAbove(underground)
                
        elif gn < 8:        
            ground = BaseZone(newtile, "Plains", "GROUND", "the plains")
            if ugn >= 2:
                underground = BaseZone(newtile, "Cave", "UNDERGROUND", "a cave")
                ground.setBelow(underground)
                underground.setAbove(ground)
                newtile.addLevel(underground)
            if (ugn >= 3) and (hpn == 0):
                #Hell tunnel time.
                underground.setBelow(hell)
                hell.setAbove(underground)
                
        else:    
            ground = BaseZone(newtile, "Town", "GROUND", "a town")
            if ugn >= 4:
                underground = BaseZone(newtile, "Catacombs", "UNDERGROUND", "The Catacombs")
                ground.setBelow(underground)
                underground.setAbove(ground)
                newtile.addLevel(underground)
            if (ugn >= 4) and (hpn <= 10):
                #Hell tunnel time.
                underground.setBelow(hell)
                hell.setAbove(underground)
                
        sky.setBelow(ground)
        ground.setAbove(sky)
        
        newtile.addLevel(ground)
        newtile.addLevel(sky)
        
        newtile.addLevel(space)
        newtile.addLevel(hell)

        #Goofiness over.
        
    def generateTilesAround(self, x, y):
        for xi in range(x-1, x+2):
            for yi in range(y-1, y+2):
                if not (xi,yi) in self.map :
                    self.generateTile(xi,yi)
            
    def getTile(self, x, y):
        return self.map[(x,y)]
