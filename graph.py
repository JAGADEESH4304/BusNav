class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.ds = float('inf')  # Distance for shortest path
        self.ts = float('inf')  # Time for shortest time
        self.cs = float('inf')  # Cost for cheapest price
        self.parent = None

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

class Graph:
    def __init__(self):
        self.Vertices = {}

    def AddVertex(self, name):
        if name not in self.Vertices:
            self.Vertices[name] = Vertex(name)

    def AddEdge(self, v1, v2, weight):
        self.AddVertex(v1)
        self.AddVertex(v2)
        self.Vertices[v1].add_neighbor(v2, weight)
        self.Vertices[v2].add_neighbor(v1, weight)

    def GetVertex(self, name):
        return self.Vertices.get(name, None)

    def load_data(self, edge_weight_file, bus_file):
        with open(edge_weight_file, 'r') as ew:
            for line in ew:
                head, tail, weight = line.strip().split()
                self.AddEdge(head, tail, float(weight))

        with open(bus_file, 'r') as bf:
            for line in bf:
                data = line.strip().split()
                bus_type = data[0]
                stops = data[1:]
                for i in range(len(stops) - 1):
                    self.AddEdge(stops[i], stops[i + 1], 1)

def DijkstrasSP(G, start, end):
    start.ds = 0
    unvisited = list(G.Vertices.values())
    while unvisited:
        current = min(unvisited, key=lambda v: v.ds)
        unvisited.remove(current)
        for neighbor, weight in current.neighbors.items():
            v = G.GetVertex(neighbor)
            if v in unvisited:
                new_distance = current.ds + weight
                if new_distance < v.ds:
                    v.ds = new_distance
                    v.parent = current.name

def PrintPath(G, s, d):
    path = []
    def recurse(v):
        if G.GetVertex(v).parent is not None:
            recurse(G.GetVertex(v).parent)
        path.append(v)
    recurse(d)
    return ' -> '.join(path)
