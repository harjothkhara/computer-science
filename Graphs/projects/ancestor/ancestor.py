# 1. Translate the problem into graph terminology

# Since we want to find the farthest parent, we'll be using DFS
# We only need to return the parent, not a path
# We only want to move towards parents


def earliest_ancestor(ancestors, starting_node):
    pass


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

# returns parents of child node
print(get_parents(ancestors, 6))  # [3,5]

# 3. Traverse the graph (BFS)
