from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue  # These may come in handy

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
flip_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
traversal_path = []  # adjacency list


def dft_walk(room, visited=None):
    # if no rooms have been visited yet...
        # assign an empty set to visited
    # assign an empty array to explored_path
    # add the current room's ID to visited
    # for each potential exit we can choose in this room ...
        # move the player to a room in direction of exit
        # if the new room hasn't been visited yet...
            # explore the new room, update visited, and check to see if its a valid path (not a dead-end)
            # if it is a valid path we move deep into the maze
                # update our current path to include valid path
            # else, not a valid path...
                # update our current path and exclude invalid path (backtrack)
            # whether the path was valid or not, add the current path to our explored path and reassign variable
    # return explored path (after all the loops and conditionals are complete)

    # assign the provided initial traversal_path variable to our explore function and pass in the player's current room to begin the game


    # TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# print traversal path
print(traversal_path)

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
