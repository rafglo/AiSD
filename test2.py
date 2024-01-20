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

    def set_distance(self, d):
        self.dist = d
    
    def get_distance(self):
        return self.dist
    
    def set_pred(self,p):
        self.pred = p

    def get_pred(self):
        return self.pred

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
        self.vertices[start].set_distance(0)
        self.vertices[start].set_pred(None)
        q = []
        q.append(start)
        while len(q):
            vert = q.pop(0)
            neighbors = self.vertices[vert].get_neighbors()
            for neighbor in neighbors:
                if not neighbor in visited:
                    q.append(neighbor)
                    visited.append(neighbor)
                    self.vertices[neighbor].set_distance(self.vertices[vert].get_distance() + 1)
                    self.vertices[neighbor].set_pred(vert)

        dists = []
        preds = []
        for vert in visited:
            preds1 = [vert]
            dists.append(self.vertices[vert].get_distance())
            pred = self.vertices[vert].get_pred()
            while pred != None:
                preds1.append(pred)
                pred = self.vertices[pred].get_pred()
            preds.append(preds1[::-1])

        return visited, dists, preds

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
    
    def shortest_paths(self, vert):
        verts, dists, paths = self.bfs(vert)
        for i in range(len(verts)):
            path = ""
            for j in range(len(paths[i])):
                if j != len(paths[i]) - 1:
                    path += str(paths[i][j]) + " -> "
                else:
                    path += str(paths[i][j])
            print("Shortest distance from " + str(vert) + " to " + str(verts[i]) + " is " + str(dists[i]) + ". Path: " + path)


G = Graph()
G.add_vertex((3,3,1))

def boat_ok(a):
    boat = a[2]
    if boat in [1,0]:
        return True
    else:
        return False
    
def missionaries_ok(a):
    mis = a[0]
    can = a[1]
    if mis in [0,1,2,3] and can in [0,1,2,3]:
        if mis >= can:
            return True
        else:
            return False
    else:
        return False
    
positions = [(1,0,1), (2,0,1), (0,1,1), (0,2,1), (1,1,1)]

run = True
past_states = []
while run:
    routes = G.bfs((3,3,1))[0]
    for route in routes:
        if len(G.get_neighbors(route)) == 0:
            for pos in positions:
                if route[2] == 0:
                    b = (route[0]+pos[0], route[1]+pos[1], route[2]+pos[2])
                    if boat_ok(b) and missionaries_ok(b):
                        if not b in past_states:
                            G.add_edge(route, b)
                            past_states.append(b)
                            if b == (0,0,0):
                                run = False
                if route[2] == 1:
                    a = (route[0]-pos[0], route[1]-pos[1], route[2]-pos[2])
                    if boat_ok(a) and missionaries_ok(a):
                        if not a in past_states:
                            G.add_edge(route, a)
                            past_states.append(a)
                            if a == (0,0,0):
                                run = False
print(G.bfs((3,3,1))[0])