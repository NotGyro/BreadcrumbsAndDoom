
from action import *

class HelpAction(Action):
    def __init__ ( self, context, commandstring=["help", "h"], helpstring = "" ) :
        self.context = context
        super(HelpAction, self).__init__(commandstring, helpstring)
    def execute(self, target=None, args="") :
        if (args == "") or (args == None):
            current = self.context
            acts = list()
            result = ""
            while not (current == None):
                acts = acts + list(current.actionDictionary.keys())
                current = current.parent
            for a in sorted(acts):
                if not (result == ""):
                    result = result + ", "
                result = result + a
            target.printer.write(result)
            return True
        commandname = args.split(" ", 1)[0]
        target.printer.write("Information on command " + commandname + ":")
        act = self.context.getAction(commandname)
        if(act == None):
            target.printer.write("Sorry, we cannot help you with that! :<")
            return False
        aliasstring = ""
        for alias in act.aliases :
            if len(aliasstring) > 0 :
                aliasstring = aliasstring + ", "
            aliasstring = aliasstring + alias
        target.printer.write("(Valid aliases: " + aliasstring + ")")
        target.printer.write(act.helpstring)
        return True
