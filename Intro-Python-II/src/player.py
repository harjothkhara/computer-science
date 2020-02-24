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
        # Grab the n/s/e/w_to attribute from the room
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

    def grab_item(self, item_name):
        item_found = False
        for item in self.current_room.items:
            #print(item)
            # looking at contents of the current room is see if the item is there
            if item.name == item_name:
                #print(item.name, user_input[1])
                # if it is there, remove from room inventory
                self.current_room.items.remove(item)
                # and add it to the player inventory
                self.inventory.append(item)
                item.on_take()
                print(
                    f"this room: {self.current_room.name} now has {self.current_room.items}\n"
                )
                # item inventory
                print(f"My items: {self.inventory}\n")
                item_found = True
                break
        if item_found is False:
            print("\nThe item you want to get/take is not in this room\n")

    def drop_item(self, item_name):
        had_item = False
        for item in self.inventory:
            #print(item)
            if item.name == item_name:
                #print(item.name, item_name)
                self.inventory.remove(item)
                self.current_room.items.append(item)
                item.on_drop()
                print(
                    f"this room: {self.current_room.name} now has {self.current_room.items}\n"
                )
                # item inventory
                print(f"My items: {self.inventory}\n")
                had_item = True
                break
        if had_item is False:
            print("\nYou do not have the item you want to drop\n")

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
