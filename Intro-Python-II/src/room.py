# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # constructor
    def __init__(self, name, description, item_list):
        # instance attributes
        self.name = name
        self.description = description
        self.item_list = item_list
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None

    def __str__(self):
        return f'Room(name: {self.name}, description: {self.description}, Item List: {self.item_list})'

    def __repr__(self):
        """
      REPR method for the Room class
      """
        return f"Room({repr(self.name)}, {repr(self.description)}, {repr(self.item_list)} )"


# second argument in Player class - current_room (Room instance below)
r = Room("Outside Cave Entrance", "North of you, the cave mount beckons",
         ['sword', 'dagger', 'knife'])
#print(r)
# current_room.name = "Outside Cave Entrance"
# current_room.description = "North of you, the cave mount beckons"
