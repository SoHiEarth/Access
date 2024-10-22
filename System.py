class System:
    def Exit():
        open(".processHistory","a").write("System/Exit\n")
        import os
        from ProgramDependent import Verbose
        if os.path.exists("SystemInfo.py"):
            os.remove("SystemInfo.py")
            open(".processHistory","a").write("System/Exit/RemovedSystemInfo\n")
        if os.path.exists("__pycache__"):
            os.remove("__pycache__")
            open(".processHistory","a").write("System/Exit/Removed__pycache__\n")
        if os.path.exists("TemporaryFile.py"):
            os.remove("TemporaryFile.py")
            open(".processHistory","a").write("System/Exit/RemovedTemporaryFile\n")
        if os.path.exists(".verb"):
            os.remove(".verb")
            open(".processHistory","a").write("System/Exit/Removed.verb\n")
        if os.path.exists(".log"):
            os.remove(".log")
            open(".processHistory","a").write("System/Exit/Removed.log\n")
        if os.path.exists(".processHistory"):
            os.remove(".processHistory")
            open(".processHistory","a").write("System/Exit/Removed.processHistory\n")
        Verbose("Closing processes","High")
        Verbose("Closed all processes, exiting","High")
        exit(0)
    def ForceExit(): 
        open(".processHistory","a").write("System/ForceExit\n")
        exit(1)
    def Help(arg):
        open(".processHistory","a").write("System/Help\n")
        if arg == "?":
            print("Exiting program...")
            System.ForceExit()
        from ProgramDependent import ThrowError
        ThrowError("exit; Exit the program.","CommandResult")
        ThrowError("help; Get all commands for the program.","CommandResult")
        ThrowError("add; Add commands to scope.","CommandResult")
        ThrowError("print; Print text.","CommandResult")
        ThrowError("scope; List all commands in scope.","CommandResult")
        ThrowError("changemode; Change the console mode.","Result")
    def Add():
        open(".processHistory","a").write("System/Add\n")
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
    def Print(Arg): 
        open(".processHistory","a").write("System/Print\n")
        print(Arg)
    def ChangeMode(Arg,Action):
        open(".processHistory","a").write("System/ChangeMode\n")
        Verb = bool(open(".verb","r").read())
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        if Arg == "": ThrowError("Change console operation modes.","Result")
        if Arg == "-v":
            if Action == "-r":
                Verb = False
                open(".verb","w").write(str(Verb))
                return
            Verb = True
            open(".verb","w").write(str(Verb))
    def ListScope():
        open(".processHistory","a").write("System/ListScope\n")
        from main import Scope
        for cmd in Scope:
            print("Command | "+str(cmd))
    Commands = ["system"]
class PlatformData:
    def OS():
        open(".processHistory","a").write("PlatformData/OS\n")
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError("OS Name | "+platform.system(),"Result")
        ThrowError("OS Ver  | "+platform.release()+" , "+platform.version(),"Result")
        ThrowError("Full OS | "+platform.platform(),"Result")
    def Arch():
        open(".processHistory","a").write("PlatformData/Arch\n")
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(str(platform.architecture()),"Result")
    def Processor():
        open(".processHistory","a").write("PlatformData/Processor\n")
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(platform.processor(),"Result")
    def Help():
        open(".processHistory","a").write("PlatformData/Help\n")
        from ProgramDependent import ThrowError
        ThrowError("Platform can detect and present system information using the platform module included with Python.","Result")
    Commands = ["OS","arch","processor","help"]
class Python:
    def Version():
        open(".processHistory","a").write("Python/Version\n")
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(platform.python_version(),"Result")
    def Branch():
        open(".processHistory","a").write("Python/Branch\n")
        from ProgramDependent import Verbose
        from ProgramDependent import ThrowError
        import platform
        Verbose("Imported platform")
        ThrowError(platform.python_branch(),"Result")
    Commands = ["version","branch"]
class Import:
    def Import(filename):
        open(".processHistory","a").write("Import/Import\n")
        from ProgramDependent import Verbose,ThrowError
        Data = open(filename,"r").read()
        ThrowError("Is this right?","Result")
        print(str(Data))
        Confirm = input("(y / n) | ")
        if Confirm == "n":
            Verbose("Action has been denied.")
            return
    def InstallNewPackage(filename):
        open(".processHistory","a").write("Import/InstallNewPackage\n")
        from ProgramDependent import Verbose,ThrowError
        newPackage = filename + ".pack"
        import os
        os.chdir()
        Data = open(newPackage,"r").read()
        if FileNotFoundError:
            ThrowError("File not found. Try again.")
            return
        print(str(Data))
        ThrowError("Is this right?","Result")
        Confirm = input("(y / n) | ")
        if Confirm == "n":
            Verbose("Action has been denied.")
            return
        open("packages.manifest","a").write("\""+filename+"\",")
        import os
        if os.path.exists("Packages") == False:
            os.chdir()
            os.mkdir("Packages")
        os.chdir("Packages")
        open(filename+".pack","w").write(Data)
        from main import Add
        Add(filename)
        ThrowError("Package successfully installed. Access it as \""+filename+"\"")
    def UpdatePackageList():
        open("packages.manifest","w").write(open(".packages","r").read())
    def PrintAllinstalledPackages():
        open(".processHistory","a").write("ProgramDependent/ReferenceCommand/console/PrintAllInstalledPackages\n")
        import os
        from ProgramDependent import ThrowError
        if os.path.exists("packages.manifest") == False:
                open("SystemInfo.py","w").write(open("SystemInfo.info","r").read())
                from SystemInfo import InstalledPackages
                for package in InstalledPackages:
                    ThrowError(package,"Result")
                return
        ThrowError("Not a native version of package manager, falling back to old.")
        ThrowError(open("packages.pack","w").write(open("packages.manifest","r").read()),"Result")
    def Version():
        open(".processHistory","a").write("ProgramDependent/ReferenceCommand/console/Version\n")
        open("SystemInfo.py","w").write(open("SystemInfo.info","r").read())
        from ProgramDependent import ThrowError
        from SystemInfo import Version
        ThrowError(str(Version),"Result")

class Internal:
    from ProgramDependent import Verbose,ThrowError
    ThrowError("Using this class is not recommended, may break the program.")
    def readVal(name):
        open(".processHistory","a").write("Internal/readVal\n")
        if name == "scope":
            from main import Scope
            for cmd in Scope: print(cmd)
        if name == "StartUpOptions":
            from main import StartUpOptions
            print(StartUpOptions)
        if name == "booted": 
            from main import Booted
            print(Booted)
        if name == "verb": print(open(".verb","r").read())
    def changeVal(name,value):
        open(".processHistory","a").write("Internal/changeVal\n")
        from main import Scope
        Scope = []
        if name == "scope":
            cmd = input("Console | ")
            while cmd != "exit":
                Scope.append(cmd)
                cmd = input("Console | ")
                if cmd == "exit": return
        if name == "StartUpOptions":
            from main import Sync
            Sync(name,value)
        if name == "booted":
            from ProgramDependent import ThrowError
            from main import Booted
            ThrowError("Altering this may crash the program.")
            import time
            time.sleep(1)
            from main import Sync
            Sync("Booted",bool(value))
def wget(url,filename):
    open(".processHistory","a").write("wget\n")
    import os
    os.system("python3 -m pip install requests")
    import requests
    if url.startswith("https://") == False:
        from ProgramDependent import Verbose
        Verbose("Adding https:// to url because connection type is not vaild...")
        url = "https://" + url
    data = requests.get(url,)
    if requests.exceptions.MissingSchema == True:
        from ProgramDependent import ThrowError
        ThrowError("Invaild URL '"+url+"': No scheme supplied.")
    open(filename,"w").write(str(data.content))
    from ProgramDependent import ThrowError
    ThrowError("Downloaded to "+os.getcwd()+"/"+filename)
Commands = ["system","platform","python","import","internal","wget"]