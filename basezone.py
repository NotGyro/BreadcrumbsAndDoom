from commandcontext import *

class BaseZone(object):
    def __init__(self, tile, name, levelName):
        self.tile = tile
        #"Name" in this case refers to a non-unique area type. For instance, typing
        #"look" in a zone named "a city" would print "You are in a city. ..."
        #The lack of an article in the default result lets you get fun stuff like
        #">look
        #You are in hell."
        self.name = name
        self.levelName = levelName
        
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
        
    def getTile(self):
        return self.tile
    def getName(self):
        return self.name
    
    
    def getCommandContext(self):
        return self.cc
    def addElement(self, name, elem):
        self.elements[name] = elem
    def removeElement(self, name):
        del self.elements[name]
    def getLook(self):
        result = "You are in " + self.name + "."
        for n, e in self.elements:
            result + e.getLook()
        if not (self.getAbove() == None):
            result = result + "\nAbove you is " + self.getAbove().getName() + "."
        if not (self.getBelow() == None):
            result = result + "\nBelow you is " + self.getBelow().getName() + "."
        return result
