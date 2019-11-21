class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbor = []
        self.status = "notvisited"
        self.discoverytime = 0
        self.finish = 0

    def add_neighbor(self,v):
        if v not in self.neighbor:
            self.neighbor.append(v)
            self.neighbor.sort()

class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, v):
        if isinstance(v , Vertex) and v not in self.vertices:
            self.vertices[v.name] = v

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if u == key:
                    value.add_neighbor(v)
                if v == key:
                    value.add_neighbor(u)
                    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+" ==>  "+ str(self.vertices[key].neighbor)+" ---> "+str(self.vertices[key].discoverytime)+"/"+str(self.vertices[key].finish))

    def dfs(self,vertex):
        global time
        time = 1
        self._dfs(vertex)
    
    def _dfs(self,vertex):
        global time
        vertex.status = "visited"
        vertex.discoverytime = time
        time += 1
        for v in vertex.neighbor:
            if self.vertices[v].status == "notvisited":
                self._dfs(self.vertices[v]) 
        vertex.status = "Finish"
        vertex.finish = time
        time += 1


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

g.dfs(a)

g.print_graph()        
        