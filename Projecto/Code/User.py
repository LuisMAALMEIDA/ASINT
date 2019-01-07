from math import sin, cos, sqrt, atan2, radians

class User:

    def __init__(self, istid, name, range):
        self.istid = istid
        self.name = name
        self.range = range
        self.latitude = float(0.0) # Atual latitude of the user
        self.longitude = float(0.0) # Atual longitude of the user
        self.LoggedIn = True

    def toDict(self):
        return {"IstID":self.istid,"Name": self.name,  "Range": self.range}

    # Verify if the user is logger in
    def LoggedIN(self):
        if(self.LoggedIn == True):
            return True
        else:
            return False

    # Define a range for a specific user
    def DefineRange(self, range):
        self.range = range

    # It verifies if this user is on the range of User X
    def InRangeOfAnotherUser(self, X_latitude, X_longitude, X_range):

        # If the user is not logged then he don't deserve to receive any message
        if( self.LoggedIn == False):
            return False

        # Approximate radius of earth in km
        R = 6373.0

        # User own latitude and longitude
        lat1 = radians(self.latitude)
        lon1 = radians(self.longitude)

        # Received latitude and longitude
        lat2 = radians(X_latitude)
        lon2 = radians(X_longitude)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c # in Km
        distanceInMeters = distance*1000 # in meters  

        if (float(X_range) - float(distanceInMeters)  >= 0 ):
            return True
        else:
            return False
