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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
flip_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
traversal_path = ['n']  # adjacency list


def dft_walk(room, visited=None):
    # if no rooms have been visited yet...
    if visited is None:
        # assign an empty set to visited (room id's)
        visited = set()
    # assign an empty array to explored_path
    explored_path = []
    # add the current room's ID to visited
    visited.add(room.id)
    # print(f"visited:{visited}")
    # for each potential exit we can choose in this room ...
    for this_exit in room.get_exits():
        # print(f"exit:{this_exit}")
        # move the player to a room in direction of exit
        new_room = room.get_room_in_direction(this_exit)
        # print(f"new-room:{new_room}")
        # if the new room hasn't been visited yet...
        if new_room.id not in visited:
            # explore the new room, update visited, and check to see if its a valid path (not a dead-end) - recursive call in chosen room.
            valid_path = dft_walk(new_room, visited)
            # if it is a valid path we move deep into the maze
            # print(f"valid-path:{valid_path}")
            if valid_path:
                # update our current path to include valid path (move deeper into maze)
                current_path = [this_exit] + valid_path + \
                    [flip_directions[this_exit]]
                # print(f"current-path:{current_path}")
            # else, not a valid path...
            else:
                # update our current path and exclude invalid path (backtrack)
                current_path = [this_exit, flip_directions[this_exit]]
                # print(f"current-path-else:{current_path}")
            # whether the path was valid or not, add the current path to our explored path and reassign variable
            explored_path = explored_path + current_path
            # print(f"explored-path:{explored_path}")
    # return explored path (after all the loops and conditionals are complete)
    return explored_path


# assign the provided initial traversal_path variable to our traversal function and pass in the player's current room to begin the game
traversal_path = dft_walk(player.current_room)


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

print("")
# print traversal path
# print(f"traversal-path: {traversal_path}")
print("")

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
