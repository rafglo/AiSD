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
                    edges.append([str(vert), str(n)])
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

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 12)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(2,1)
g.add_edge(3, 4)
g.add_edge(4, 7)
g.add_edge(4, 12)
g.add_edge(7, 8)
print(g.topological_sort())