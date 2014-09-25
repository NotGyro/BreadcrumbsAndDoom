#python3.4

"""A strange text RPG about birds. Beware all ye who enter here."""

import world
import maptile
import combatengine
from action import *
from commandcontext import *
from help import *

class TestAct(Action):
    def execute(self, target=None, args="") :
        print("Whahey, " + args + "!")
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
