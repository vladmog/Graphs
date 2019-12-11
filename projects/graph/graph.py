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
        if vertex_id in self.vertices:
            print("Key already in dict")
        else:
            self.vertices[vertex_id] = set()
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            visiting = q.dequeue()
            if visiting not in visited:
                print(visiting)
                visited.add(visiting)
                visiting_neighbors = self.get_neighbors(visiting)
                for neighbor in visiting_neighbors:
                    q.enqueue(neighbor)

        pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            visiting = s.pop()
            if visiting not in visited:
                print(visiting)
                visited.add(visiting)
                visiting_neighbors = self.get_neighbors(visiting)
                for neighbor in visiting_neighbors:
                    s.push(neighbor)

        pass  # TODO


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if visited has been initialized
        if visited is None:
            # If not, initialize to an empty set
            visited = set()
        # Mark the node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # Call DFT recursive on each neighbor that has not been visited
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

        pass  # TODO



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited...
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_vert)
                # Then add A PATH TO its neighbors to the back of the queue
                neighbors = self.get_neighbors(last_vert)
                for neighbor in neighbors:
                    # COPY THE PATH
                    path_copy = path.copy()
                    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push( [starting_vertex] )
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the  PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited...
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_vert)
                neighbors = self.get_neighbors(last_vert)
                # Then add A PATH TO its neighbors to the top of the stack
                for neighbor in neighbors:
                    # COPY THE PATH
                    path_copy = path.copy()
                    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(neighbor)
                    s.push(path_copy)


        pass  # TODO

    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Init visited
        if visited is None:
            visited = set()
        # Init path
        if path is None:
            path = []
        visited.add(starting_vertex)
        # Add vertex to the path
        # path.append(starting_vertex)    << Why is this different than the next line
        path = path + [starting_vertex]
        # If we are at the target value, return the path
        if starting_vertex == target_vertex:
            print("Thinks it found the target")
            return path
        # Otherwise, call DFS_recursive on each unvisited neighbor
        else:
            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    var = self.dfs_recursive(neighbor, target_vertex, visited, path)
                    if var is not None:
                        return var
            return None





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
    print(graph.vertices)


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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

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
    print("TEST")
    print(graph.dfs_recursive(1, 6))
    print("TEST")
