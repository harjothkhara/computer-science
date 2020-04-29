
import random
from util import Stack, Queue  # These may come in handy
# 1. Translate the problem into graph terminology:
# users are nodes, edges are friendships and undirected (bi-directional friendship), cyclic, problem mentions shortest friendship path between users extended netword (BFS)


# Your client is also interested in how the performance will scale as more users join so she has asked you to implement a feature that creates large numbers of users to the network and assigns them a random distribution of friends.

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return repr(self.name)


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}  # adjacency list -  graph stores a list of vertices and for each vertex, a list of each vertex to which its connected
        # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}...}

    def add_friendship(self, user_id, friend_id):  # created randomly
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        # checking adjacency list for existing friendship from both sides
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:  # creares bi-directional friendship
            # e.g user 1 is friends with user 5
            self.friendships[user_id].add(friend_id)
            # e.g user 5 is friends with user 1
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        # e.g inside users dict -> key:1 value:User 1
        self.users[self.last_id] = User(name)
        # e.g inside friendships dict -> key:1 value:empty set, or set()
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        # time complexity = O(n)^2
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}  # adjacency list
        # !!!! IMPLEMENT ME

        # Creates that number of users - Add users
        # Write a for loop that calls add_user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i+1}")  # e.g User 1, User 2...

        # Creating randomly distributed  friendships between those users
        # To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, then grab the first N elements from the list. You will need to import random to get shuffle.create a list with all possible friendships

        # generate all friendship combinations
        possible_friendships = []
        # avoid duplicates by making sure first number is smaller than second
        for user_id in self.users:  # e.g for user 4 we only care about user 5,6,7 ...
            # don't want to ignore last
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle all possible friendships
        random.shuffle(possible_friendships)

        # create for first X pairs x is total //2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # every possible friendship that could exist in our network
        print(f"possible friendships: {possible_friendships}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME

        #  translate to graph terminology - (shortest path tells us BFS)
        #  extended network - traversal, connected component

        # planning
        # how are we going to build a graph? we done did that one
        # start at given user id, do a bft, return the path to each friend

        # create a queue
        q = Queue()
        # enqueue path
        q.enqueue([user_id])
        # create visited
        visited = {}  # Note that this is a dictionary, not a set
        # while queue not empty
        while q.size() > 0:
            # dequeue first path
            path = q.dequeue()
            vertex = path[-1]
            # if not visited
            if vertex not in visited:
                # do the thing!
                # add to visited
                visited[vertex] = path  # {1: {8, 10, 5}, 2: {10, 5, 7}
                # for each neighbor (we have the whole graph in frienships and don't have to go searching for neighbors of current vertex like before)
                for neighbor in self.friendships[vertex]:
                    # copy path and enqueue
                    new_path = path.copy()
                    new_path.append(neighbor)
                    q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("")
    print(f"users:{sg.users}")  # {1: User 1, 2: User 2...}
    print("")
    print(f"friendships:{sg.friendships}")
    # {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set(), 10: set()}
    print("")
    connections = sg.get_all_social_paths(1)
    print(f"extended-network: {connections}")
