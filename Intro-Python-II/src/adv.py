from item import Item
from room import Room
from player import Player
import textwrap
import sys

# Create the REPL command parser in adv.py which allows the player to move to rooms in the four cardinal directions.
# REPL = Read, Evaluate, Print, Loop

# Declare all the rooms
# room dictionary with key:value--> an instance of the class Room

k = Item("keys", "An ancient gold key that shines with an ethereal shinner.")
#print(k)
# Item(name: Keys, description: An ancient gold key that shines with an ethereal shinner.
s = Item(
    "sword",
    "Those sparks during battles are REAL! Our knights use real weapons - even swords made from titanium!"
)
d = Item("dagger",
         "a small sharp pointy thing that protects Monty Python from evil")
r = Item("revolver",
         "perpendicular looking handgun with a chamber barrel for firing")
w = Item("wrench", "used to apply torque to turn an object")

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons",
         'no item'),
    'foyer':
    Room(  # dict value is an instance of the Room class
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [s]),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [d]),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [r]),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [w]),
}

# Link rooms together
# current_room  attribute - does the users current_room contain this directional attribute? Association - "has-a" relationship. Room has a direction attribute.
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main

# Make a new player object that is currently in the 'outside' room.

player_name = input("What is your name? ")
p = Player(player_name, room['outside'], [])
# Room(name: Outside Cave Entrance, description: North of you, the cave mount beckons) <--- used str method in Room class

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#textwrap.fill(text[, width[, ...]])

# current_room == Room instance
print(f'\nReady {p.name}\n')
print(f"You are currently at {p.current_room.name}\n")
print(f"My items: {p.inventory}\n")

while True:

    user_input = input("enter directions:(n)orth, (s)outh, (e)ast. (w)est \n"
                       "choose action: get/take item, drop item\n"
                       "or (q)uit:\n"
                       "~~~~> ").strip().lower().split()

    # print(user_input, f"hello")

    # collecting items commands
    if len(user_input) == 2:
        #print("we have an item in here")
        if user_input[0] == 'get' or user_input[0] == 'take':
            item_found = False
            for item in p.current_room.items:
                #print(item)
                # looking at contents of the current room is see if the item is there
                if item.name == user_input[1]:
                    #print(item.name, user_input[1])
                    # if it is there, remove from room inventory
                    p.current_room.items.remove(item)
                    # and add it to the player inventory
                    p.inventory.append(item)
                    item.on_take()
                    # item inventory
                    print(f"My items: {p.inventory}\n")
                    item_found = True
                    break
            if item_found is False:
                print("The item you want to get/take is not in this room")
        elif user_input[0] == 'drop':
            had_item = False
            for item in p.inventory:
                print(item)
                if item.name == user_input[1]:
                    print(item.name, user_input[1])
                    p.inventory.remove(item)
                    p.current_room.items.append(item)
                    item.on_drop()
                    had_item = True
                    break
            if had_item is False:
                print("You do not have the item you want to drop")
        else:
            print(
                "command not recognized. 'get or take' to add an item or 'drop' to drop  an item"
            )

    # direction commands
    elif len(user_input) == 1:
        # char length of fist list item to make sure its 'n, s, e, w
        #print(user_input, "inside user_input 1")
        if len(user_input[0]) > 1:
            print('unknown command', len(user_input[0]))
            break
        if user_input[0] in ['n', 's', 'e', 'w']:
            # move to that room
            p.travel(user_input[0])
        else:
            print('\nNOT A VALID MOVE\n')

    # Read
    # Evaluate
    # Print
    # Loop

# hasattr() - The hasattr() method returns true if an object has the given named attribute and false if it does not. hasattr(object, name).
# getattr() - returns the value of the name attribute of the given object, and not a boolean. e.g
# r = class Room: ..... /////
# >>> r.s_to = "yolo"
# >>> getattr(r, 's_to')
# 'yolo'
# object - object whose named attribute is to be checked
# name - name of the attribute to be searched
