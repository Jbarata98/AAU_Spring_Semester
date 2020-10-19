import json
import customTypes

# Open file and read JSON data as dictionaries
dataFile = open("SmallDataSetExamples.json", "r+")
data = json.load(dataFile)

# Initialize empty objects
dataObjects = []
tempObject = customTypes.DataObject()

# Loop through all objects extracted from the file and
# keep only the data that is of interest.
for tweet in data:
    tempObject = customTypes.DataObject()
    if tweet['text'] != '':
        tempObject.text = tweet['text']
    if tweet['lang'] != '':
        tempObject.lang = tweet['lang']

    # Create a geo object and fill it's fields
    # Then assign newly created object to dataObject.geo field
    tempGeo = customTypes.Geo()
    if tweet['geo'] != None:
        tempGeo.geoType = tweet['geo']['type']
        tempGeo.coordinates = tweet['geo']['coordinates']
        tempObject.geo = tempGeo

    # Create a place object and fill it's fields
    # Then assign newly created object to dataObject.place field
    tempPlace = customTypes.Place()
    if tweet['place'] != None:
        tempBox = customTypes.BoundingBox()
        if tweet['place']['bounding_box'] != None:
            tempBox.boxType = tweet['place']['bounding_box']['type']
            tempBox.coordinates = tweet['place']['bounding_box']['coordinates']
        tempPlace.boundingBox = tempBox
        tempPlace.placeType = tweet['place']['place_type']
        tempPlace.name = tweet['place']['name']
        tempPlace.fullName = tweet['place']['full_name']
        tempPlace.country = tweet['place']['country']
        tempPlace.countryCode = tweet['place']['country_code']
        tempObject.place = tempPlace

    # Append newly created dataObject to list
    dataObjects.append(tempObject)

counter = 0
geoCounter = 0
placeCounter = 0

for dataObject in dataObjects:
    counter += 1
    print(f'Object number {counter}.:')
    print(f'\tobject.text: {dataObject.text}')
    print(f'\tobject.lang: {dataObject.lang}')
    if dataObject.geo != None:
        geoCounter += 1
        print(f'\t\tobject.geo.geoType: {dataObject.geo.geoType}')
        print(f'\t\tobject.geo.coordinates {dataObject.geo.coordinates}')
    else:
        print('This object does not have geo data.')
    if dataObject.place != None:
        placeCounter += 1
        print(f'\t\tobject.place.placeType: {dataObject.place.placeType}')
        print(f'\t\tobject.place.name: {dataObject.place.name}')
        print(f'\t\tobject.place.country: {dataObject.place.country}')
        if dataObject.place.boundingBox != None:
            print(f'\t\t\tobject.place.boundingBox.boxType: {dataObject.place.boundingBox.boxType}')
            print(f'\t\t\tobject.place.boundingBox.coordinates: {dataObject.place.boundingBox.coordinates}')
        else:
            print('This object does not have bouding box data.')
    else:
        print('This object does not have place data.')

print(f'There are {counter} objects.')
print(f'{geoCounter} objects have geo data and {placeCounter} have place data.')
