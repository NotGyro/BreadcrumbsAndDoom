#python3.4

#ba dum tch
class Action(object):
    #This constructor takes either a string to use as the command /
    #key for players to type, or a list of aliases for the command.
    #Thus, Action("attack") and Action(["Attack", "A", "Atk"]) are
    #both valid.
    def __init__ ( self, commandstring, helpstring = "" ) :
        #Will this never be used, and instead kept to copy?
        self.isTemplate = False
        self.aliases = []
        self.helpstring = helpstring
        #If our command string is any container of multiple strings, add them.
        if(isinstance(commandstring, (tuple, list, set))):
            self.aliases.extend(commandstring)
        else:
            #If our command string is a single string, cause aliases to
            #contain it and it alone. 
            self.aliases = [commandstring]
    #Target refers to the entity being controlled.
    def execute(self, target=None, args="") :
        print("Action.execute(args) is a dummy function, please inherit the class.")
        return False
