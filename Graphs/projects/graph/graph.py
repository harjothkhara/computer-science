"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # inserting a key:value into vertices dict. key is the vertex number and the value is a set()
        self.vertices[vertex_id] = set()
        #  key: value
        # { 5: set(), 8: set(), 9: set()...}

    def add_edge(self, v1, v2):  # adding edges to our set
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        Traversal = visiting each vertex in the graph
        """
        # Create a queue - FIFO
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all of its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

# queue = [2,3]
# visited = {1}

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        Traversal = visiting each vertex in the graph
        """
        # create a stack - LIFO
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to stored visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # Pop the last vertex in
            v = s.pop()
            # Check if it's been visited
            # If is hasn't been visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all of its neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # for initial function call
        if visited is None:
            visited = set()
        # Check if the node has been visited = handled by our default arg when we recurse.
        # print adjacent vertex during recursive call which will then become the starting_vertex
        print(starting_vertex)
        # add adjacent vertex to visited set
        visited.add(starting_vertex)

        # check neighboring vertices for our current vertex, if none start returning down stack
        for neighbor in self.get_neighbors(starting_vertex):
            # check if neighbors have been visited
            if neighbor not in visited:
                # call dft_recursive on each neighbor - now visited!
                self.dft_recursive(neighbor, visited)

########## Another way ##########
# if visited is None:
#   visited = set()
# -check if the node has been visited
# -if not,
# if starting vertex not in visited:
#   -mark it as visited
#   visited.add(starting_vertex)
#   print(starting_vertex)
#   -call dft_recursive on each neighbor
#   for neighbor in self.get_neighbors(starting_vertex):
#       self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue - FIFO
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            print(f"Queue: {q}")
            # Dequeue the first PATH
            path = q.dequeue()
            print(f"Path: {path}")
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            print(f"vertex at end of path: {v}")
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Mark it as visited
                visited.add(v)
                print(f"visited: {visited}")

                # Enqueue A PATH TO all of its neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    # deep copy pass by value vs pass by reference. arrays are pass by reference, hence we need to make a new copy of the old path before we append to it. also, path.copy() works
                    path_copy = list(path)
                    # ADD NEIGHBOR TO NEW PATH
                    path_copy.append(neighbor)
                    # ENQUEUE THE COPY OF THE PATH
                    q.enqueue(path_copy)

                # target = 6
                # q = [ [1,2,4,7], [1,2,3,5,3] ]
                 # visited = {1,2,3,4,5}
                 # path = [1,2,4,6]
                 # v = 6
                 # path_copy = [1,2,3,5,3]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order. Same code as bfs except we're using a different data structure - a stack instead of a queue.
        """
        # Create a stack - LIFO
        s = Stack()
        # Push A PATH TO the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            print(f"Stack: {s}")
            # Pop the first PATH
            path = s.pop()
            print(f"Path: {path}")
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            print(f"vertex at end of path: {v}")
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Mark it as visited
                visited.add(v)
                print(f"visited: {visited}")

                # Push A PATH TO all of its neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    # deep copy pass by value vs pass by reference. arrays are pass by reference, hence we need to make a new copy of the old path before we append to it. also, path.copy() works
                    path_copy = list(path)
                    # ADD NEIGHBOR TO NEW PATH
                    path_copy.append(neighbor)
                    # PUSH THE COPY OF THE PATH
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(F"Graph: {graph.vertices}")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # print("BFT")
    # graph.bft(1)  # starting vertex

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print("DFT")
    # graph.dft(1)  # starting vertex

    # print("DFT Recursive")
    # graph.dft_recursive(1)  # starting vertex

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
