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
        edges = {}
        for vert in self.vertices:
            neighbors = self.vertices[vert].get_neighbors()
            if not neighbors is None:
                for n in neighbors:
                    edges[vert] = n
        return edges

g = Graph()
g.add_vertex("a")
g.add_edge("a", "b")
print(g.get_edges())