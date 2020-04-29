from util import Stack, Queue
# what does this graph represent? hierarchial parent child relationship

# 1. Translate the problem into graph terminology

# Since we want to find the farthest parent, we'll be using DFS
# We only need to return the parent, not a path
# We only want to move towards parents
# more than one ancestor return one with lowest numeric id
# no parents return -1


# 2: Build the Graph


def get_parents(ancestors, child):
    results = []
    # print(f"ancestors: {ancestors}")
    for node in ancestors:
        # if child is in graph
        if child == node[1]:
            # add the parents to the list
            results.append(node[0])
    return results


# Our Graph, or given dataset (parent, child)
ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

'''
        10
      /
     1   2   4  11
      \ /   / \ /
       3   5   8
        \ / \   \
         6   7   9
     '''

# returns parents of child node
# print(f"parents: {get_parents(ancestors, 6)}")  # [3,5]

# 3. Traverse the graph (BFS)


def earliest_ancestor(ancestors, starting_node):
    # create a set for children with parents, fast lookup, no duplicates
    child_set = set()  # {1 3 5 6 7 8 9}
    for node in ancestors:
        # add child to set
        child_set.add(node[1])
    # if starting_node not in child_list then it doesn't have a parent, return -1
    print(f"child_set: {child_set}")
    if starting_node not in child_set:
        return -1
    # traverse our graph for oldest ancestor - farthest distance - DFS. checked that our staring_node is indeed a child.
    else:
        # create an empty stack - LIFO
        s = Stack()
        # push the starting node (a path) into the stack
        s.push([starting_node])
        # create a set to store visited vertices
        visited = set()
        # while there is something in the stack
        while s.size() > 0:
            print(f"Stack: {s}")
            # remove the first path from the stack
            path = s.pop()  # [path...]
            print(f"Path: {path}")
            # grab the vertex from the end of the path (child we will check)
            v = path[-1]
            print(f"vertex at end of path: {v}")
            # check if it's been visited
            # if it hasn't been visited...
            if v not in visited:
                # mark it as visited and add it to the visited set
                visited.add(v)
                print(f"visited: {visited}")
            # get a list of parents for the current node - use our helper fn!
            for parent in get_parents(ancestors, v):
                print(f"parent: {parent}")
                # make a copy of the path
                path_copy = path.copy()
                # append that parent node to the path_copy
                path_copy.append(parent)
                # push the path copy into the stack
                s.push(path_copy)
        # return earliest ancestor - after the starting_node(child),parent will always be the last node on our path
        return path[-1]


# print(earliest_ancestor(ancestors, 1))  # 10
# print(earliest_ancestor(ancestors, 2))  # -1
# print(earliest_ancestor(ancestors, 3))  # 10
# print(earliest_ancestor(ancestors, 4))  # -1
# print(earliest_ancestor(ancestors, 5))  # 4
print(earliest_ancestor(ancestors, 6))  # 10
# print(earliest_ancestor(ancestors, 7))  # 4
# print(earliest_ancestor(ancestors, 8))  # 4
# print(earliest_ancestor(ancestors, 9))  # 4
# print(earliest_ancestor(ancestors, 10))  # -1
# print(earliest_ancestor(ancestors, 11))  # -1
