class Graph:
    def __init__(self, txt) -> None:
        with open(txt) as f:
            self.V = int(f.readline())
            self.E = int(f.readline())
            self.adj = [[] for i in range(self.V)]
            for i in range(self.V):
                edge = f.readline()
                vertices = [int(v) for v in edge.split()]
                self.add_edge(vertices[0], vertices[1])
    
    def adj_vertices(self, v):
        return self.adj[v]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def print(self):
        print('{} vertices {} edges.'.format(self.V, self.E))
        for v in range(self.V):
            s = '{}: '.format(v)
            for w in self.adj_vertices(v):
                s += '{} '.format(w)
            print(s)


if __name__ == "__main__":
    graph = Graph('data/tinyG.txt')
    graph.print()
