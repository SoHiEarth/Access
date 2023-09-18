class System:
    def Exit():
        from ProgramDependent import Verbose
        Verbose("Closing processes","High")
        Verbose("Closed all processes, exiting","High")
        exit(0)
    def ForceExit():
        exit(1)
    def Help(arg):
        if arg == "?":
            print("Exiting program...")
            System.ForceExit()
        from ProgramDependent import ThrowError
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
            open(".verb","w").write(str(Verb))
            Verbose("Changed mode to Verb")
        if Mode == "!Verb":
            if Verb == False:
                ThrowError("Mode is already normal.")
                return
            Verb = False
            open(".verb","w").write(str(Verb))
            Verbose("Changed mode to normal")
    def ListScope():
        from main import Scope
        for cmd in Scope:
            print("Command | "+str(cmd))
    Commands = ["exit","help","add","print","scope"]
class PlatformData:
    def OS():
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError("OS Name | "+platform.system(),"Result")
        ThrowError("OS Ver  | "+platform.release()+" , "+platform.version(),"Result")
        ThrowError("Full OS | "+platform.platform(),"Result")
    def Arch():
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(str(platform.architecture()),"Result")
    def Processor():
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(platform.processor(),"Result")
    def Help():
        from ProgramDependent import ThrowError
        ThrowError("Platform can detect and present system information using the platform module included with Python.","Result")
    Commands = ["OS","Arch","Processor","Help"]
class Python:
    def Version():
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(platform.python_version(),"Result")
    def Branch():
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(platform.python_branch(),"Result")
    Commands = ["Version","Branch"]
class Import:
    def Import(filename):
        from ProgramDependent import Verbose,ThrowError
        Data = open(filename,"r").read()
        ThrowError("Is this right?","Result")
        print(str(Data))
        Confirm = input("(y / n) | ")
        if Confirm == "n":
            Verbose("Action has been denied.")
            return


def wget(url,filename):
    import os
    os.system("python3 -m pip install requests")
    import requests
    data = requests.get(url)
    open(filename,"w").write(data.content)
    from ProgramDependent import ThrowError
    ThrowError("Downloaded to "+os.getcwd()+"/"+filename)
Commands = ["wget"]
