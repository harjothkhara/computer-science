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

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            # pop last vertex on the stack
            v = s.pop()
        # Check if the node has been visited
        # If not...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)  # add it to our visited set
                # Call dft_recursive on each neighbor

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue - FIFO
        # Enqueue A PATH TO the starting vertex
        # Create a set to store visited vertices
        # While the queue is not empty...
        # Dequeue the first PATH
        # GRAB THE VERTEX FROM THE END OF THE PATH
        # Check if it's been visited
        # If it hasn't been visited...
        # Mark it as visited
        # CHECK IF IT'S THE TARGET
        # IF SO, RETURN THE PATH
        # Enqueue A PATH TO all of its neighbors
        # MAKE A COPY OF THE PATH
        # ENQUEUE THE COPY
# target = 6
# q = [ [1] ]
# visited = {}

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

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
    print("BFT")
    graph.bft(1)  # starting vertex

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT")
    graph.dft(1)  # starting vertex
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
