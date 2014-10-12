from commandcontext import *

class BaseZone(object):
    def __init__(self, tile, name, levelName, lookText=""):
        self.tile = tile
        #"Name" in this case refers to a non-unique area type. For instance, typing
        #"look" in a zone named "a city" would print "You are in a city. ..."
        #The lack of an article in the default result lets you get fun stuff like
        #">look
        #You are in hell."
        self.name = name
        self.levelName = levelName
        if (lookText=="") or (lookText==None):
            self.lookName = self.name
        else:
            self.lookName = lookText
        
        self.elements = dict()
        self.above = None
        self.below = None
        #CommandContext stuff goes here.
        self.cc = CommandContext()
    
    
    def setAbove(self, ab):
        self.above = ab
    def setBelow(self, bel):
        self.below = bel
    def getAbove(self):
        return self.above
    def getBelow(self):
        return self.below

    def getLevel(self):
        return self.levelName
        
    def getTile(self):
        return self.tile
    def getName(self):
        return self.name
    def getLookName(self):
        return self.lookName

    def getEast(self):
        xTo = self.tile.x+1
        yTo = self.tile.y
        return self._getNear(xTo, yTo)
    def getNorth(self):
        xTo = self.tile.x
        yTo = self.tile.y+1
        return self._getNear(xTo, yTo)
    def getWest(self):
        xTo = self.tile.x-1
        yTo = self.tile.y
        return self._getNear(xTo, yTo)
    def getSouth(self):
        xTo = self.tile.x
        yTo = self.tile.y-1
        return self._getNear(xTo, yTo)

    #Internal function to cut down on copy-pasting.
    #Treats this zone->tile->world->tile->zone thing as
    #if it were manually walking through a linked list.
    def _getNear(self, xTo, yTo):
        current = self.getTile()
        if current == None :
            return None

        current = current.getWorld()
        if current == None :
            return None

        current = current.getTile(xTo, yTo)
        if current == None :
            return None

        current = current.getLevel(self.levelName)
        if current == None :
            return None

        return current
    
    
    def getCommandContext(self):
        return self.cc
    def addElement(self, name, elem):
        self.elements[name] = elem
    def removeElement(self, name):
        del self.elements[name]
    def getLook(self):
        result = "You are in " + self.getLookName() + "."
        for n, e in self.elements:
            result + e.getLook()
        if not (self.getAbove() == None):
            result = result + "\nAbove you is " + self.getAbove().getLookName() + "."
        if not (self.getBelow() == None):
            result = result + "\nBelow you is " + self.getBelow().getLookName() + "."
            
        if not (self.getEast() == None):
            result = result + "\nTo the East is " + self.getEast().getLookName() + "."
        if not (self.getNorth() == None):
            result = result + "\nTo the North is " + self.getNorth().getLookName() + "."
        if not (self.getWest() == None):
            result = result + "\nTo the West is " + self.getWest().getLookName() + "."
        if not (self.getSouth() == None):
            result = result + "\nTo the South is " + self.getSouth().getLookName() + "."
        return result
