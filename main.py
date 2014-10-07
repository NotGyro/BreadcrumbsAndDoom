#python3.4

"""A strange text RPG about birds. Beware all ye who enter here."""

from world import *
import maptile
import combatengine
import sys
from action import *
from commandcontext import *
from help import *
from player import *

class TestAct(Action):
    def execute(self, target=None, args="") :
        print("Whahey, " + args + "!")
        return True

class QuitAction(Action):
    def execute(self, target=None, args="") :
        print("Quitting...")
        sys.exit()
        return True

print("Hello again, world. How ya doin'?")

testContext = CommandContext()
print (testContext.doCommand("rolf -a")) #Should print False.
a = Action(["Attack", "A", "Atk"], "do some shit")

b = TestAct(["test", "t"], "WHAHEY")

h = HelpAction(testContext)

testContext.addAction(a)
testContext.addAction(b)
testContext.addAction(h)

print(testContext.doCommand("aTk JUNK DaTa")) #Should print true.
print(testContext.doCommand("t user"))
testContext.doCommand("h t")

q = QuitAction(["Quit","Exit","q"])
testContext.addAction(q)

testWorld = World()
testWorld.generateTile(0,0)

testPlayer = PlayerCharacter()

tile = testWorld.getTile(0,0)
ground = tile.getLevel("GROUND")
hell = BaseZone(tile, "hell", "HELL")
ground.setBelow(hell)
hell.setAbove(ground)
tile.addLevel("HELL", hell)

testPlayer.setCurrentZone(ground)
testContext.setParent(testPlayer.getCommandContext())
while True:
    inputcmd = input('>')
    if not testContext.doCommand(inputcmd, testPlayer):
        print("Error: '" + inputcmd + "' is not a valid command.")
