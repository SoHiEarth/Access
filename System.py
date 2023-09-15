class System:
    def Exit():
        exit(0)
    def Help():
        from main import ThrowError
        ThrowError("exit; Exit the program.","CommandResult")
        ThrowError("help; Get all commands for the program.","CommandResult")
        ThrowError("add; Add commands to scope.","CommandResult")
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
            AddedCommands = input("Console | ")

    Commands = ["exit","help","add"]