import graphviz, sys
class Vertex():
    def __init__(self, key):
        self.id = key
        self.neighbors = {}

    def add_neighbor(self, value, weight):
        self.neighbors[value] = weight
    
    def __str__(self):
        return "Node: " + str(self.id) + " Neighbors: " + str([i.id for i in self.neigbors])

    def get_neighbors(self):
        return [i.id for i in self.neighbors]
    
    def get_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.neighbors[neighbor]


class Empty(Exception):
    pass

class Queue:
    DEFAULT_CAPACITY = 10
    K = 0.2

    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        if self._size <= Queue.K * len(self._data):
            self.resize(len(self._data) // 2)
        return value

    def enqueue(self,e):
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self,cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size): #only existing elements
            self._data[k] = old[walk]
            walk = (1 + walk)%len(old)
        self._front = 0 

    def __str__(self):
        """elements = [(self._data[(self._front + i) % len(self._data)]) for i in range(self._size)]
        return f"Queue: {elements}"
        """
        result = []
        for i in range(len(self._data)):
            if self._data[(self._front + i)%len(self._data)] is None:
                result.append(" ")
            else:
                result.append(self._data[(self._front + i)%len(self._data)])
        return str(result)

from collections import deque

class Graph(Vertex):
    def __init__(self):
        self.vertices = {}
        self.size = 0

    def add_vertex(self, vert_key):
        vertex = Vertex(vert_key)
        self.vertices[vert_key] = vertex
        self.size += 1
        return vertex
    
    def __contains__(self, vert_key):
        return vert_key in self.vertices
    
    def vertex(self, vert_key):
        if vert_key in self.vertices:
            return self.vertices[vert_key]
        else:
            return None
        
    def get_neighbors(self, vert_key):
        if vert_key in self.vertices:
            return self.vertices[vert_key].get_neighbors()
        else:
            return None

    def get_vertices(self):
        return [x for x in self.vertices]
    
    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertices:
            self.add_vertex(from_key)
        if to_key not in self.vertices:
            self.add_vertex(to_key)
        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)
    
    def get_edges(self):
        edges = []
        for vert in self.vertices:
            neighbors = self.vertices[vert].get_neighbors()
            if not neighbors is None:
                for n in neighbors:
                    edges.append(str(vert) + str(n))
        return edges
    
    def visualize(self):
        dot = graphviz.Digraph()
        for vert in self.vertices:
            dot.node(str(vert), str(vert))
        for edge in self.get_edges():
            dot.edge(str(edge[0]), str(edge[1]))
        return dot
        
    def bfs(self, start):
        visited = [start]
        q = []
        q.append(start)
        while len(q):
            vert = q.pop()
            neighbors = self.vertices[vert].get_neighbors()
            for neighbor in neighbors:
                if not neighbor in visited:
                    q.append(neighbor)
                    visited.append(neighbor)
        return visited

    def dfs(self, start, visited = []):
        if not start in visited:
            visited.append(start)
        neighbors = self.vertices[start].get_neighbors()
        for neighbor in neighbors:
            if not neighbor in visited:
                self.dfs(neighbor, visited)
        return visited

    def dfs_topological_sort(self, start, stack, visited = []):
        if not start in visited:
            visited.append(start)
        neighbors = self.vertices[start].get_neighbors()
        for neighbor in neighbors:
            if not neighbor in visited:
                self.dfs_topological_sort(neighbor, stack, visited)
        stack.append(start)

    def topological_sort(self):
        visited = []
        stack = []

        for vert in self.get_vertices():
            if not vert in visited:
                self.dfs_topological_sort(vert, stack, visited)
        
        return stack[::-1]

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4,6)
g.add_edge(6,9)
g.add_edge(6,10)
g.add_edge(2, 5)
print(g.bfs(2))
print(g.dfs(2))
g.visualize()
print(g.topological_sort())