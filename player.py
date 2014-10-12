from livingentity import *
from commandcontext import *
from action import *
from dumbprinter import *

class DescendAction(Action):
    def execute(self, target=None, args="") :
        target.descend();
        return True
class AscendAction(Action):
    def execute(self, target=None, args="") :
        target.ascend();
        return True

class LookAction(Action):
    def execute(self, target=None, args="") :
        target.printer.write(target.zone.getLook())
        return True

class GoAction(Action):
    def execute(self, target=None, args="") :
        target.go(args)
        return True


class PlayerCharacter:
    def __init__(self):
        #TODO
        self.healthpoints = 100
        self.cc = CommandContext()
        self.zone = None
        self.tile = None
        self.printer = DumbPrinter()
        self.cc.addAction(AscendAction(["Ascend","a","u","Up"],"Go up."))
        self.cc.addAction(DescendAction(["Descend","d","Down"],"Go down."))
        self.cc.addAction(LookAction(["Look","l"],"""Take a look around.
Adding an argument specifies an object in the current context to look at."""))
        self.cc.addAction(GoAction(["Go","g","travel","fly","f"],"""Go to any place specified by the command's argument."""))
        #Is this player playing on this machine, instead of just
        #connecting to this server?
        self.local = True
    def setCurrentZone(self, zone):
        self.zone = zone
        self.cc.setParent(zone.getCommandContext())
        self.setCurrentTile(zone.getTile())

        tile = zone.getTile()
        tile.getWorld().generateTilesAround(tile.x, tile.y)
    def setCurrentTile(self, tile):
        self.tile = tile
    def getCommandContext(self):
        return self.cc

    def ascend(self):
        if not (self.zone == None):
            if not (self.zone.getAbove() == None):
                self.setCurrentZone(self.zone.getAbove())
                self.printer.write("You have ascended to " + self.zone.getLookName() + ".")
            else:
                self.printer.write("Cannot fly any higher here.")
        else:
            self.printer.write("Error: Character isn't in any zone!")
    def descend(self):
        if not (self.zone == None):
            if not (self.zone.getBelow() == None):
                self.setCurrentZone(self.zone.getBelow())
                self.printer.write("You have descended to " + self.zone.getLookName() + ".")
            else:
                self.printer.write("Cannot fly any lower here.")
        else:
            self.printer.write("Error: Character isn't in any zone!")
    def go(self, direction):
        if not (self.zone == None):
            direction = direction.upper()
            if direction == "EAST":
                if not ( self.zone.getEast() == None):
                    self.setCurrentZone(self.zone.getEast())
                    self.printer.write("You fly East to " + self.zone.getLookName() + ".")
                else:
                    self.printer.write("You cannot go East from here.")
            elif direction == "NORTH":
                if not ( self.zone.getNorth() == None):
                    self.setCurrentZone(self.zone.getNorth())
                    self.printer.write("You fly North to " + self.zone.getLookName() + ".")
                else:
                    self.printer.write("You cannot go North from here.")
            elif direction == "WEST":
                if not ( self.zone.getWest() == None):
                    self.setCurrentZone(self.zone.getWest())
                    self.printer.write("You fly West to " + self.zone.getLookName() + ".")
                else:
                    self.printer.write("You cannot go West from here.")
            elif direction == "SOUTH":
                if not ( self.zone.getSouth() == None):
                    self.setCurrentZone(self.zone.getSouth())
                    self.printer.write("You fly South to " + self.zone.getLookName() + ".")
                else:
                    self.printer.write("You cannot go South from here.")
            elif direction == "UP":
                self.ascend()
            elif direction == "DOWN":
                self.descend()
            else:
                #Placeholder: Going into buildings and such soon.
                self.printer.write("Cannot fly any lower here.")
        else:
            self.printer.write("Error: Character isn't in any zone!")
