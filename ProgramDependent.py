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
def ReferenceCommand(Input):
    from main import Scope
    from System import System
    Parent = ""
    Child = ""
    for i in range(len(Input)):
        if Input[i] == ":":
            i += 1  # Move to the next character after ":"
            while i < len(Input) and Input[i] != ":" and Input[i] != " ":
                Child += Input[i]
                i += 1
            break
        else:
            Parent += Input[i]
    if Parent not in Scope:
        return
    
    if Parent == "exit":
        if Child == "":
            System.Exit()
        if Child == "ForceExit":
            System.ForceExit()
        
    if Input == "help":
        System.Help(Child)

    if Input == "add":
        System.Add()

    if Input == "print":
        System.Print()

    if Input == "scope":
        System.ListScope()

    if Input == "ChangeMode":
        System.ChangeMode()
        
    if Parent == "Platform":
        from System import PlatformData
        if Child == "OS":
            PlatformData.OS()