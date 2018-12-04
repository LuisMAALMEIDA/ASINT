class User:

    def __init__(self, istid, range):
        self.istid = istid
        self.range = range

    def toDict(self):
        return {"IstID":self.istid, "Range": self.range}

