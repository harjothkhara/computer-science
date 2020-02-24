# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    # constructor
    def __init__(self, name, description, items=[]):
        # instance attributes
        self.name = name
        self.description = description
        self.items = items
        # defaults to null until we check for a valid association
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'Room(name: {self.name}, description: {self.description}, items: {[item.name for item in self.items]})'

    def __repr__(self):
        """
      REPR method for the Room class
      """
        return f"Room({repr(self.name)}, {repr(self.description)}, {repr(self.items)} )"


k = Item("Keys", "An ancient gold key that shines with an ethereal shinner.")
#print(k)
s = Item(
    "Sword",
    "Those sparks during battles are REAL! Our knights use real weapons - even swords made from titanium!"
)

# second argument in Player class - current_room (Room instance below)
r = Room("Outside Cave Entrance", "North of you, the cave mount beckons",
         [k, s])

#print(r)
# current_room.name = "Outside Cave Entrance"
# current_room.description = "North of you, the cave mount beckons"
