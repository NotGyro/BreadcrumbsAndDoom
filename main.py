#python3.4

"""A strange text RPG about birds. Beware all ye who enter here."""

import world
import maptile
import combatengine
from action import *
from commandcontext import *

print("Hello again, world. How ya doin'?")

testContext = CommandContext()
print (testContext.doCommand("rolf -a")) #Should print False.
a = Action(["Attack", "A", "Atk"], "do some shit")
testContext.addAction(a)
print(testContext.doCommand("aTk JUNK DaTa"))
