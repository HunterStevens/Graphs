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
        self.vertices[vertex_id] = set()
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 not in self.vertices:
            print("The start Vertex with that id doesn't exist.")
        else:
            print("The destination vertex with that id doesn't exist")
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)

                for nxt in self.get_neighbors(v):
                    q.enqueue(nxt)
        return visited
        # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stck = Stack()
        visited = set()
        stck.push(starting_vertex)

        while stck.size() > 0:
            v = stck.pop()
            if v not in visited:
                visited.add(v)
                print(v)

                for nxt in self.get_neighbors(v):
                    stck.push(nxt)
        return visited
        # TODO

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for nxt in self.get_neighbors(starting_vertex):
                self.dft_recursive(nxt, visited)
        # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        que = Queue()
        que.enqueue([starting_vertex])
        visited = set()

        while que.size() > 0:
            ver = que.dequeue()
            prev_ver = ver[-1]
            if prev_ver not in visited:
                if prev_ver == destination_vertex:
                    return ver
                else:
                    visited.add(prev_ver)
                for nxt in self.get_neighbors(prev_ver):
                    copy_path = ver.copy()
                    copy_path.append(nxt)
                    que.enqueue(copy_path)

        # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stck = Stack()
        stck.push([starting_vertex])
        visited = set()

        while stck.size() > 0:
            ver = stck.pop()
            prev_ver = ver[-1]
            if prev_ver not in visited:
                if prev_ver == destination_vertex:
                    return ver
                else:
                    visited.add(prev_ver)
                for nxt in self.get_neighbors(prev_ver):
                    copy_path = ver.copy()
                    copy_path.append(nxt)
                    stck.push(copy_path)
        # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, ver = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if ver is None:
            ver = []
            ver.append(starting_vertex)
        
        if ver[-1] not in visited:
            if ver[-1] == destination_vertex:
                return ver
            else:
                visited.add(starting_vertex)
            for nxt in self.get_neighbors(starting_vertex):
                copy_path = list(ver)
                copy_path.append(nxt)
                nxt_path = self.dfs_recursive(nxt, destination_vertex, visited, copy_path)
                if nxt_path is not None:
                    return nxt_path
        

        # TODO

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

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    print("\n")
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    print("\n")
    graph.dft(1)
    print("\n")
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print("\n")
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print("\n")
    print(graph.dfs(1, 6))
    print("\n")
    print(graph.dfs_recursive(1, 6))
