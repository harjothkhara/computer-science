# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap


class Player:
    # constructor
    def __init__(self, name, starting_room, inventory=[]):
        # instance attributes
        self.name = name
        self.current_room = starting_room
        self.inventory = inventory  # items

    def travel(self, direction):
        # is there an association attached to current_room
        # room['outside']    .n  _to
        next_room = getattr(self.current_room, f"{direction}_to")
        #print(next_room, "next_room")  # returns next room
        #print(current_room, "current_room")
        #print(user_input[0], "user input")
        # if there is an association attached to current_room
        if next_room is not None:
            #room['outside'] = room['outside'].n_to
            self.current_room = next_room
            # give me name attribute on the Room instance
            print(f"You are currently at {self.current_room.name}\n")
            # give me item_list attribute on the Room instance
            print(textwrap.fill(self.current_room.description, 50), '\n')
            print(
                f"This room has the following items: {self.current_room.items}\n"
            )
            print(f"My items: {self.inventory}\n")
        else:
            print('\nyou cannot move in that direction\n')

    def __str__(self):
        """
        Replacement string method for the Player class
        """
        return f"The current player is {self.name} and they are in {self.current_room}"

    def __repr__(self):
        """
        REPR method for the Player class
        """
        return f"Player({repr(self.name)})"
