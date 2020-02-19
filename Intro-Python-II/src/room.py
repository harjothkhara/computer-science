# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # constructor
    def __init__(self, name, description):
        # instance attributes
        self.name = name
        self.description = description
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None


r = Room("Outside Cave Entrance", "North of you, the cave mount beckons")
#print(r.description)
