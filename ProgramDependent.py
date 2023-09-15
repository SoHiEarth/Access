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