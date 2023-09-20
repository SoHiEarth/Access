def ThrowError(Error,Type="NewError"):
    if Type == "NewError":
        print("Error   | "+Error)
    if Type == "CommandResult" or "Result":
        print("Result  | "+Error)
def Verbose(Input,Priority = "Low"):
    from datetime import datetime
    now = datetime.now()
    Verb = bool(open(".verb","r").read())
    open(".log","a").write(now.strftime("%m/%d/%Y, %H:%M:%S")+str(Input)+"\n")
    if Verb == False or "False":
        return
    if Priority == "High" or "high":
        print("Message | Priority " + Priority + ": " + Input + "...")
        return
    print("Message | Priority " + Priority + ":    " +Input + "...")
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
        if Child == "Python":
            from System import Python
            from main import Scope
            Scope.append(Python.Commands)
            Verbose("Successfully imported System.Python.Commands to Scope.","High")
            ThrowError("Successful.","Result")
            return
        if Child == "Essentials":
            from System import System
            from main import Scope
            Scope.append(System.Commands)
            Verbose("Successfully imported System.System.Commands to Scope.","High")
            ThrowError("Successful.","Result")
            return
        if Child == "PlatformData":
            from System import PlatformData
            from main import Scope
            Scope.append(PlatformData.Commands)
            Verbose("Successfully imported System.PlatformData.Commands to Scope.","High")
            ThrowError("Successful.","Result")
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

    if Parent == "import":
        from System import Import
        Import.Import(Child)
    
    if Parent == "newVariable":
        CurrentVariable = Child
        open(".VariableStore","w").write(CurrentVariable)
        Verbose("Data "+str(Child)+" has been stored as a variable.","High")

    if Parent == "readVariable":
        ThrowError(open(".VariableStore","r").read(),"Result")
        Verbose("Presented readVariable")

    if Parent == "changeVariable":
        CurrentVariable = Child
        open(".VariableStore","w").write(CurrentVariable)
        Verbose("Data "+str(Child)+" has been stored as a variable.","High")
    
    if Parent == "Mode":
        if Child == "Change":
            System.ChangeMode()
        if Child == "Display":
            print(open(".verb","r").read())