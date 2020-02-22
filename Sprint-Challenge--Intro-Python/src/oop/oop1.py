# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# base class
class Vehicle:
    # constructor
    def __init__(self):
        # attributes
        pass


class GroundVehicle(Vehicle):
    # constructor
    def __init__(self):
        pass
    # inherited attributes
    # super().__init__()


class Car(GroundVehicle):
    # constructor
    def __init__(self):
        pass
    # # inherited attributes
    # super().__init__()


class Motorcycle(GroundVehicle):
    # constructor
    def __init__(self):
        pass
    # inherited attributes
    # super().__init__()


class FlightVehicle(Vehicle):
    # constructor
    def __init__(self):
        pass
    # inherited attributes
    # super().__init__()


class Airplane(FlightVehicle):
    # constructor
    def __init__(self):
        pass
    # inherited attributes
    # super().__init__()


class Starship(FlightVehicle):
    # constructor
    def __init__(self):
        pass
    # inherited attributes
    # super().__init__()
