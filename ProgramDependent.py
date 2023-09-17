def ThrowError(Error,Type="NewError"):
    if Type == "NewError":
        print("Error   | "+Error)
    if Type == "CommandResult" or "Result":
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
        ThrowError("Command \""+Parent+"\" not in scope")
        return
    
    if Parent == "exit":
        if Child == "":
            System.Exit()
        if Child == "ForceExit":
            System.ForceExit()
        
    if Parent == "help":
        System.Help(Child)

    if Parent == "add":
        if Child == "System":
            from System import Commands
            from main import Scope
            Scope.append(Commands)
            Verbose("Successfully imported System.Commands to Scope.","High")
            ThrowError("Successful.","Result")
            return
        System.Add()

    if Parent == "print":
        System.Print()

    if Parent == "scope":
        System.ListScope()

    if Parent == "ChangeMode":
        System.ChangeMode()

    if Parent == "Platform":
        from System import PlatformData
        if Child == "":
            PlatformData.Help()
        if Child == "OS":
            PlatformData.OS()
        if Child == "arch":
            PlatformData.Arch()
        if Child == "Processor":
            PlatformData.Processor()
    if Parent == "Python":
        from System import Python
        if Child == "Version":
            Python.Version()
        if Child == "Branch":
            Python.Branch()
    if Parent == "wget":
        if Child == "" or None:
            ThrowError("State a child.")
            return
        from System import wget
        filename = input("Name?   | ")
        wget(Child,filename)
