class Building:
	def __init__(self, id, name, latitude, longitude, radius):
		self.id = id
		self.name = name
		self.latitude = latitude
		self.longitude = longitude
		self.radius = radius

	def toDict(self):
		return {"BuildingID": self.id, "Name": self.name, "Latitude": self.latitude, "Longitude": self.longitude, "Radius": self.radius}
