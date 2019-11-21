class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = []
        self.distance = 0
        self.color = 'Black'
    def add_neighbors(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
class Graph:
    vertices = {}
    def add_vertex(self , v):
        if isinstance(v , Vertex) and v.name not in self.vertices:
            self.vertices[v.name] = v
            return True
        else:
            return False
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            for key, value in self.vertices.items():
                if key == v1:
                    value.add_neighbors(v2)
                if key == v2:
                    value.add_neighbors(v1)
            return True
        else:
            return False
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+" ==>  "+str(self.vertices[key].neighbors))  

g = Graph()
g.add_vertex(Vertex('a'))
g.add_vertex(Vertex('b'))
g.add_vertex(Vertex('c'))
g.add_vertex(Vertex('d'))
g.add_vertex(Vertex('e'))
g.add_edge('a','b')
g.add_edge('a','c')
g.add_edge('a','e')
g.add_edge('b','e')
g.add_edge('c','d')
g.add_edge('d','e')


g.print_graph()