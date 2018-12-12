class User:

    def __init__(self, istid, name, range):
        self.istid = istid
        self.name = name
        self.range = range
        self.LoggedIn = True

    def toDict(self):
        return {"IstID":self.istid,"Name": self.name,  "Range": self.range}
    
    # Verify if the user is logger in
    def LoggedIN(self):
        if(self.LoggedIn == True):
            return True
        else:
            return False

    def DefineRange(self, range):
        self.range = range

