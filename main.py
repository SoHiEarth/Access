import os
import sys
import datetime
print("Console Interpreter v0.1")
Booted = False
StartUpOptions = input("Press SPACE to continue...")
if StartUpOptions == "Verb":
    Verb = True
    Booted = True
else:
    Booted = True
    Verb = False
if Verb == True:
    print("Initializing Variables...")
def Verbose(Input, Priority = "Low"):
    if Verb == False:
        return
    if Priority == "High":
        print("Priority " + Priority + ":  " + Input + "...")
        return
    print("Priority " + Priority + ":   " +Input + "...")
Verbose("Initializing Variables")

# Init. Var
Importeddatetime = True
Importedsys = True
Importedos = True
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