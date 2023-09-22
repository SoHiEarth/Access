def ThrowError(Error,Type="NewError"):
    open(".processHistory","a").write("Error\n")
    if Type == "NewError":
        print("Error   | "+Error)
    if Type == "CommandResult" or "Result":
        print("Result  | "+Error)
def Verbose(Input,Priority = "Low"):
    Verb = bool(open(".verb","r").read())
    if Verb == False or "False":
        return
    if Priority == "High":
        print("Message | Priority " + Priority + ": " + Input + "...")
        return
    print("Message | Priority " + Priority + ":    " +Input + "...")
def ReferenceCommand(Input):
    open(".processHistory","a").write("RefCommand\n")
    from main import Scope
    from System import System
    Parent = ""
    Child = ""
    args = ""
    subargs = ""
    i = 0  # Initialize the index outside the loop

    while i < len(Input):
        if Input[i] == ":":
            i += 1  # Move to the next character after ":"
            while i < len(Input) and Input[i] != ":" and Input[i] != " ":
                Child += Input[i]
                i += 1
            if i < len(Input) and Input[i] == ":":
                i += 1  # Move to the next character after the second ":"
                while i < len(Input) and Input[i] != ":" and Input[i] != " ":
                    args += Input[i]
                    i += 1
                if i < len(Input) and Input[i] == ":":
                    i += 1  # Move to the next character after the third ":"
                    while i < len(Input) and Input[i] != ":" and Input[i] != " ":
                        subargs += Input[i]
                        i += 1
            break
        else:
            Parent += Input[i]
            i += 1
    if Parent not in Scope:
        ThrowError("Command \""+Parent+"\" not in scope")
        return
    if Parent == "system":
        if Child == "exit":
            if args == "": System.Exit()
            if args == "ForceExit": System.ForceExit() 
        if Child == "help": System.Help(args)
        if Child == "add":
            if args == "System":
                from System import Commands
                from main import Scope
                Scope.append(Commands)
                Verbose("Successfully imported System.Commands to Scope.","High")
                ThrowError("Successful.","Result")
                return
            if args == "Python":
                from System import Python
                from main import Scope
                Scope.append(Python.Commands)
                Verbose("Successfully imported System.Python.Commands to Scope.","High")
                ThrowError("Successful.","Result")
                return
            if args == "Essentials":
                from System import System
                from main import Scope
                Scope.append(System.Commands)
                Verbose("Successfully imported System.System.Commands to Scope.","High")
                ThrowError("Successful.","Result")
                return
            if args == "PlatformData":
                from System import PlatformData
                from main import Scope
                Scope.append(PlatformData.Commands)
                Verbose("Successfully imported System.PlatformData.Commands to Scope.","High")
                ThrowError("Successful.","Result")
            System.Add()
        if Child == "print": System.Print(args)
        if Child == "scope": System.ListScope()
        if Child == "changemode": System.ChangeMode(args,subargs)
    if Parent == "platform":
        from System import PlatformData
        if Child == "": PlatformData.Help()
        if Child == "OS": PlatformData.OS()
        if Child == "arch": PlatformData.Arch()
        if Child == "processor": PlatformData.Processor()
        if Child == "help": PlatformData.Help()
    if Parent == "python":
        from System import Python
        if Child == "version": Python.Version()
        if Child == "branch": Python.Branch()
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