
from action import *

class HelpAction(Action):
    def __init__ ( self, context, commandstring=["help", "h"], helpstring = "" ) :
        self.context = context
        super(HelpAction, self).__init__(commandstring, helpstring)
    def execute(self, target=None, args="") :
        if (args == "") or (args == None):
            print(self.context.actionDictionary)
            return True
        commandname = args.split(" ", 1)[0]
        print("Information on command " + commandname + ":")
        act = self.context.getAction(commandname)
        if(act == None):
            print("Sorry, we cannot help you with that! :<")
            return False
        aliasstring = ""
        for alias in act.aliases :
            if len(aliasstring) > 0 :
                aliasstring = aliasstring + ", "
            aliasstring = aliasstring + alias
        print("(Valid aliases: " + aliasstring + ")")
        print(act.helpstring)
        return True
