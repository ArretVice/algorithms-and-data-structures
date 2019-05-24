import graph as g 


class WeightedGraph(g.Graph):
    def __init__(self):
        super().__init__()
        self.edges = {}

    def add_edge(self, start_vertex, end_vertex, weight=1):
        if super().add_edge(start_vertex, end_vertex):
            self.edges[start_vertex.name + end_vertex.name] = weight
            return True 
        return False


letters = 'ABCDEF'
edges = 'AB AC BC BD CD CE DF ED EF'.split(' ')
weights = [2, 5, 8, 7, 2, 4, 1, 6, 3]

def populate_weighted_graph(vertices, edges, weights):
    # example weighted graph 1
    c = WeightedGraph()
    for letter in vertices:
        vertex = g.Vertex(letter, content=letter.lower())
        c.add_vertex(vertex)
    for edge, weight in zip(edges, weights):
        c.add_edge(c.vertices[edge[0]], c.vertices[edge[1]], weight)

    print(f'Root: {c.root}')
    print(f'Vertices: {list(c.vertices.keys())}')
    print(f'Edges: {c.edges}\n')
    return c


if __name__ == '__main__':
    print(populate_weighted_graph(letters, edges, weights))
