import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    # constructor
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)
    # for readability

    def __str__(self):
        return f"{self.name}: {self.lat}, {self.lon}"


#c = City("London", -43.34, 45.67)
# print(c)

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. --> City("San Francisco", 67.23, -25.65)

# Then return the list with all the City instances from the function. ---> append each instance of City to cities list

# Google "python 3 csv" for references and use your Google-fu for other examples.
#
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

# --> fields = key (unique), rows = value

cities = []
# mycities = []


# def mycityreader(mycities=[]):
#     with open('cities.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             #print(row['city'], row['lat'], row['lng'])
#             # Seattle 47.6217 -122.3238

#             # City instance
#             c = City(row['city'], row['lat'], row['lng'])
#             # adding to mycities list
#             mycities.append(c)
#         # be careful - don't want to return just a single row(city-Seatle)
#         return mycities

# mycityreader(mycities)

# for city in mycities:
#     print(city)


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open('cities.csv', newline='') as csvfile:  # opening
        reader = csv.DictReader(csvfile)  # reading file as a dict
        # print(reader)
        for row in reader:  # filtering each row to match City class instance
            # Store the instances in the "cities" list, below.
            #  each record is imported into a City instance
            # City class instance with column key (dict:key value)
            cities.append(City(row["city"], row["lat"], row['lng']))

    return cities


# calling function
cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    # print(c)

    # STRETCH GOAL!
    #
    # Allow the user to input two points, each specified by latitude and longitude.
    # These points form the corners of a lat/lon square. Pass these latitude and
    # longitude values as parameters to the `cityreader_stretch` function, along
    # with the `cities` list that holds all the City instances from the `cityreader`
    # function. This function should output all the cities that fall within the
    # coordinate square.
    #
    # Be aware that the user could specify either a lower-left/upper-right pair of
    # coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
    # the input data so that it's always one or the other, then search for cities.
    # In the example below, inputting 32, -120 first and then 45, -100 should not
    # change the results of what the `cityreader_stretch` function returns.
    #
    # Example I/O:
    #
    # Enter lat1,lon1: 45,-100
    # Enter lat2,lon2: 32,-120
    # Albuquerque: (35.1055,-106.6476)
    # Riverside: (33.9382,-117.3949)
    # San Diego: (32.8312,-117.1225)
    # Los Angeles: (34.114,-118.4068)
    # Las Vegas: (36.2288,-115.2603)
    # Denver: (39.7621,-104.8759)
    # Phoenix: (33.5722,-112.0891)
    # Tucson: (32.1558,-110.8777)
    # Salt Lake City: (40.7774,-111.9301)

    # TODO Get latitude and longitude values from the user

    def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
        # within will hold the cities that fall within the specified region
        within = []

        # TODO Ensure that the lat and lon valuse are all floats
        # Go through each city and check to see if it falls within
        # the specified coordinates.

        return within
