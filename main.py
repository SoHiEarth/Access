print("Console Interpreter v0.11")
Booted = False
StartUpOptions = input("Press SPACE to continue...")
Verb = False
AddAllCommands = False
if "-v" in StartUpOptions:
    Verb = True
elif "-a" in StartUpOptions:
    AddAllCommands = True
Booted = True
open(".verb","w").write(str(Verb))
if Verb == True:
    print("Initializing Variables...")
from ProgramDependent import Verbose as Verbose
Verbose("Initializing Variables")
# Init. Var
Importeddatetime = True
Importedsys = True
Importedos = True
from System import System
Verbose("Imported Library \"System\"")
Scope = []
Verbose("Scope Initialized")
Scope = Scope + System.Commands
Verbose("New scope from System added to current scope","Low")
# Init. Def
from ProgramDependent import ReferenceCommand as Interpreter
Verbose("Imported Interpreter")
def Add(Target):
    Scope.append(Target)
Verbose("Initialized Add")
if AddAllCommands == True:
    Verbose("Commands from System being added to scope","High")
    from ProgramDependent import ReferenceCommand
    ReferenceCommand("add:System")
    ReferenceCommand("add:Python")
    ReferenceCommand("add:Essentials")
    ReferenceCommand("add:PlatformData")
    Verbose("Added all commands from System to scope","High")
if (Importeddatetime == True) & (Importedos == True) & (Importedsys == True):
    NoErrors = True
    Verbose("Import Check Complete, No errors found.")
else:
    NoErrors = False
    Verbose("Import Check INCOMPLETE, an error has been found.", "High")
if NoErrors == True:
    Verbose("Initialized Variables", "Low")
if NoErrors == False:
    Verbose("Error when initializing variables", "High")   
if Booted == True & NoErrors == True:
    Verbose("Startup Complete.", "High")
while Booted == True:
    cmd = input("Console | ")
    Interpreter(cmd)