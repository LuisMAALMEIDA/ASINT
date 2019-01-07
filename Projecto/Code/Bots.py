class Bot:
    def __init__(self, id, building_id):
        self.id = id
        self.building_id = building_id

    def toDict(self):
        return {"ID": self.id, "BuildingID" : self.buiding_id}
