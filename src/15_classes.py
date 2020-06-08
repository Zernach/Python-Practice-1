# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f"Lat={self.lat}\nLon={self.lon}"

latlon = LatLon(50, 70)
print(latlon.__str__())

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return f"\nLat={self.lat}\nLon={self.lon}\nName={self.name}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

waypoint = Waypoint(name='Catacombs', lat=41.70505, lon=-121.51521)
print(waypoint.__str__())

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return f"\nLat={self.lat}\nLon={self.lon}\nName={self.name}\nDifficulty={self.difficulty}\nSize={self.size}"

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geo = Geocache(lat=44.05, lon=-121.4, name="Newberry Views", difficulty=1.5, size=2)

# Print it--also make this print more nicely
print(geo.__str__())
