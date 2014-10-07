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


class PlayerCharacter:
    def __init__(self):
        #TODO
        self.healthpoints = 100
        self.cc = CommandContext()
        self.zone = None
        self.tile = None
        self.printer = DumbPrinter()
        self.cc.addAction(AscendAction(["Ascend","a","u","Up"],"Go up."))
        self.cc.addAction(DescendAction(["Descend","d""Down"],"Go down."))
        self.cc.addAction(LookAction(["Look","l"],"""Take a look around.
Adding an argument specifies an object in the current context to look at."""))
        #Is this player playing on this machine, instead of just
        #connecting to this server?
        self.local = True
    def setCurrentZone(self, zone):
        self.zone = zone
        self.cc.setParent(zone.getCommandContext())
        self.setCurrentTile(zone.getTile())
    def setCurrentTile(self, tile):
        self.tile = tile
    def getCommandContext(self):
        return self.cc
    def ascend(self):
        if not (self.zone == None):
            if not (self.zone.getAbove() == None):
                self.setCurrentZone(self.zone.getAbove())
                self.printer.write("You have ascended to " + self.zone.getName() + ".")
            else:
                self.printer.write("Cannot fly any higher here.")
        else:
            self.printer.write("Error: Character isn't in any zone!")
    def descend(self):
        if not (self.zone == None):
            if not (self.zone.getBelow() == None):
                self.setCurrentZone(self.zone.getBelow())
                self.printer.write("You have descended to " + self.zone.getName() + ".")
            else:
                self.printer.write("Cannot fly any lower here.")
        else:
            self.printer.write("Error: Character isn't in any zone!")
