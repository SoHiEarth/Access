class System:
    def Exit():
        from ProgramDependent import Verbose
        Verbose("Closing processes","High")
        Verbose("Closed all processes, exiting","High")
        exit(0)
    def ForceExit():
        exit(1)
    def Help():
        from main import ThrowError
        ThrowError("exit; Exit the program.","CommandResult")
        ThrowError("help; Get all commands for the program.","CommandResult")
        ThrowError("add; Add commands to scope.","CommandResult")
        ThrowError("print; Print text.","CommandResult")
        ThrowError("scope; List all commands in scope.","CommandResult")
    def Add():
        from ProgramDependent import ThrowError
        from ProgramDependent import Verbose
        from main import Scope
        AddedCommands = input("AddScope| Enter new commands here to add to scope, exit by using exit.\nAddScope| ")
        while AddedCommands != "exit":
            if AddedCommands == "exit":
                return
            if AddedCommands in Scope:
                ThrowError("This command \""+AddedCommands+"\" is already in the current scope")
                Verbose("Command already in scope","High")
            else:
                Scope.append(AddedCommands)
            AddedCommands = input("AddScope| ")
    def Print():
        Content = input("Print   | ")
        print(Content)
    def ChangeMode():
        from main import Verb
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        Mode = input("System  | ChangeMode to :")
        if Mode == "Verb":
            if Verb == True:
                ThrowError("Mode is already Verb.")
                return
            Verb = True
            Verbose("Changed mode to Verb")
        if Mode == "!Verb":
            if Verb == False:
                ThrowError("Mode is already normal.")
                return
            Verb = False
            Verbose("Changed mode to normal")
    def ListScope():
        from main import Scope
        for cmd in Scope:
            print("Command | "+cmd)
    Commands = ["exit","help","add","print","scope"]
class PlatformData:
    def OS():
        from ProgramDependent import Verbose
        import platform
        Verbose("Imported platform")
        print("OS Name | "+platform.system())
        print("OS Ver  | "+platform.release()+" , "+platform.version())
        print("Full OS | "+platform.platform())