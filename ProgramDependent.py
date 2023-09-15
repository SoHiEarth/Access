def ThrowError(Error,Type="NewError"):
    if Type == "NewError":
        print("Error   | "+Error)
    if Type == "CommandResult":
        print("Result  | "+Error)
def Verbose(Input, Priority = "Low", ):
    from main import Verb as Verb
    if Verb == False:
        return
    if Priority == "High":
        print("Priority " + Priority + ":  " + Input + "...")
        return
    print("Priority " + Priority + ":   " +Input + "...")
def ReferenceCommand(Input:str):
    from main import Scope
    from System import System
    if Input not in Scope:
        ThrowError("Command: \""+Input+"\" not in scope.")
        return
    if Input == "exit":
        System.Exit()
    if Input == "help":
        System.Help()
    if Input == "add":
        System.Add()
    if Input == "print":
        System.Print()
    if Input == "Scope":
        System.ListScope()
    if Input == "ChangeMode":
        System.ChangeMode()