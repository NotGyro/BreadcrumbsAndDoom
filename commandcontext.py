from action import *

#To which commands are directed 
class CommandContext(object):
    def __init__(self, pset = None):
        self.actionDictionary = dict()
        self.parent = pset
    def setParent(self, pset):
        self.parent = pset
    def addAction(self, act):
        for al in act.aliases:
            #Convert to uppercase for case-insensitivity
            self.actionDictionary[al.upper()] = act
    #Returns true if a command was matched, false if not.
    def doCommand(self, cmdstr, cmdTarget=None):
        #Get the first word in the command, all uppercase
        splitcmd = cmdstr.split(" ", 1)
        first = splitcmd[0].upper()
        if first in self.actionDictionary:
            #Command exists.
            if len(splitcmd) > 1:
                #We have arguments, pass them on through.
                return self.actionDictionary.get(first).execute(target=cmdTarget, args=(splitcmd[1]))
            else:
                #No command arguments.
                return self.actionDictionary.get(first).execute(target=cmdTarget)
            #A command was found and executed
        else:
            #No command matching:
            if not ( self.parent == None ):
                return self.parent.doCommand(cmdstr, cmdTarget)
            return False
    def getAction(self, act):
        if (act == None) or (act == ""):
            print("ERROR: Invalid action - cannot retrieve nil command!")
            return None
        if act.upper() in self.actionDictionary:
            return self.actionDictionary.get(act.upper())
        if not (self.parent == None):
            return self.parent.getAction(act)
        print("Command not found.")
        return None
