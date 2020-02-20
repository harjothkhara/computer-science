from item import Item
from room import Room
from player import Player
import textwrap
import sys

# Create the REPL command parser in adv.py which allows the player to move to rooms in the four cardinal directions.
# REPL = Read, Evaluate, Print, Loop

# Declare all the rooms
# room dictionary with key:value--> an instance of the class Room

k = Item("Keys", "An ancient gold key that shines with an ethereal shinner.")
#print(k)
# Item(name: Keys, description: An ancient gold key that shines with an ethereal shinner.
s = Item(
    "Sword",
    "Those sparks during battles are REAL! Our knights use real weapons - even swords made from titanium!"
)
d = Item("Dagger",
         "a small sharp pointy thing that protects Monty Python from evil")
r = Item("Revolver",
         "perpendicular looking handgun with a chamber barrel for firing")
w = Item("Wrench", "used to apply torque to turn an object")

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons",
         [k.name]),
    'foyer':
    Room(  # dict value is an instance of the Room class
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [s.name]),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [d.name]),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [r.name]),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [w.name]),
}

# Link rooms together
# current_room  attribute - does the users current_room contain this directional attribute?
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
p = Player(player_name, room['outside'])
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
while True:

    print(f'Ready {p.name}\n')
    # give me name attribute on the Room instance
    print(f"You are currently at {p.current_room.name}\n")
    # give me item_list attribute on the Room instance
    print(f"This room has the following items: {p.current_room.item_list}\n")
    print(textwrap.fill(p.current_room.description, 50), '\n')

    user_input = input(
        "what direction do you want to move? n, s, e, or w \n ~~~~> ").strip(
        ).lower().split()

    print(user_input, f"hello")

    if len(user_input) == 2:
        print("we have an item in here")

    if len(user_input) == 1:
        # char length of fist list item to make sure its 'n, s, e, w
        print(user_input, "inside user_input 1")
        if len(user_input[0]) > 1:
            print('unknown command', print(len(user_input[0])))
            break
        if user_input[0] == 'q' or user_input == 'quit':
            print('\n // GAME OVER\n')
            sys.exit(0)
        elif user_input[0] == 'n':
            if hasattr(p.current_room, 'n_to'):
                p.current_room = p.current_room.n_to
            else:
                print('you cannot enter')
        elif user_input[0] == 's':
            if hasattr(p.current_room, 's_to'):
                p.current_room = p.current_room.s_to
            else:
                print('you cannot enter')
        elif user_input[0] == 'e':
            if hasattr(p.current_room, 'e_to'):
                p.current_room = p.current_room.e_to
            else:
                print('you cannot enter')
        elif user_input[0] == 'w':
            if hasattr(p.current_room, 'w_to'):
                p.current_room = p.current_room.w_to
            else:
                print('you cannot enter')
        else:
            print('NOT A VALID MOVE\n')

    # Read
    # Evaluate
    # Print
    # Loop

# hasattr() - The hasattr() method returns true if an object has the given named attribute and false if it does not. hasattr(object, name).
# object - object whose named attribute is to be checked
# name - name of the attribute to be searched
