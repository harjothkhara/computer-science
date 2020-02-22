# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


# base class
class GroundVehicle:
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # methods
    def drive(self):
        return f"vroooom"


g = GroundVehicle().drive()
# print(g)

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO


class Motorcycle(GroundVehicle):
    # constructor
    def __init__(self):
        # inherited attributes from super class
        # set number of wheels to 2 by passing it to the constructor of Motorcycle superclass
        super().__init__(num_wheels=2)
        # any specific attributes for Motorcyle class

    # method (overidding)
    def drive(self):
        super().drive()
        return f"BRAAAP!!"


m = Motorcycle().drive()
# print(m)

# list called 'vehicles' that is called instances of the both classes
vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
for vehicle in vehicles:
    print(vehicle.drive())
