class DataObject:
    def __init__(self, text=None, lang=None, geo=None, coordinates=None, place=None):
        self.text = text
        self.lang = lang
        self.geo = geo
        self.coordinates = coordinates
        self.place = place

class Geo:
    def __init__(self, geoType=None, coordinates=None):
        self.geoType = geoType
        self.coordinates = coordinates

class Place:
    def __init__(self, placeType=None, name=None, fullName=None, countryCode=None, country=None, boundingBox=None):
        self.placeType = placeType
        self.name = name
        self.fullName = fullName
        self.countryCode = countryCode
        self.country = country
        self.boundingBox = boundingBox

class BoundingBox:
    def __init__(self, boxType=None, coordinates=None):
        self.boxType = boxType
        self.coordinates = coordinates
