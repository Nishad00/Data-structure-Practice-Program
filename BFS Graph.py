class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = []
        self.distance = 0
        self.color = 'Black'
    def add_neighbors(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
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
            print(key+" ==>  "+str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)
		
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'
			
            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
        



g = Graph()
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('A','E')
g.add_edge('B','E')
g.add_edge('C','D')
g.add_edge('D','E')

g.bfs(a)

g.print_graph()