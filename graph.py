import random
import string


class Graph:
    def __init__(self):
        self.vertices = {}
        self.root = None

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            if not self.root:
                self.root = vertex
            return True
        return False

    def add_edge(self, start_vertex, end_vertex):
        if (start_vertex.name in self.vertices) and (end_vertex.name in self.vertices):
            if end_vertex not in start_vertex.nearest_vertices:
                self.vertices[start_vertex.name].nearest_vertices.append(end_vertex)
                return True
        return False

    def __str__(self):
        return f'Graph with {len(self.vertices)} nodes and starts at node {self.root.name}'


class Vertex:
    def __init__(self, name, content=None):
        self.name = name
        self.content = content
        self.nearest_vertices = []

    def __str__(self):
        return f'Node {self.name}'


def populate_graph(graph, vertices):
    random_lowercase_letters = string.ascii_lowercase
    random_numbers = string.digits
    for start, end in vertices:
        if start not in graph.vertices:
            start_vertex = Vertex(start)
            graph.add_vertex(start_vertex)
        else:
            start_vertex = graph.vertices[start]
        if end not in graph.vertices:
            end_vertex = Vertex(end)
            graph.add_vertex(end_vertex)
        else:
            end_vertex = graph.vertices[end]
        if not start_vertex.content:
            start_vertex.content = random.choice(random_lowercase_letters)
        if not end_vertex.content:
            end_vertex.content = random.choice(random_numbers)
        graph.add_edge(start_vertex, end_vertex)
    print('\n=== Graph populated ===')
    print(graph)
    print(f'Vertices: {[vertex for vertex in graph.vertices]}')
    print(f'Edges: {vertices}')
    print('=== ===== ========= ===\n')
    return graph

example_graph1 = ['AB', 'AC', 'AF', 'CD', 'CF', 'DE', 'FE']
example_graph2 = 'AB AC AD BE BF CG GH HI HJ HK'.split(' ')

if __name__ == '__main__':
    vertices = example_graph1
    graph = Graph()
    graph = populate_graph(graph, vertices)
    print(f'Graph starts at {graph.root.name}')
    for vertex in graph.vertices:
        print(f'Vertex: {vertex} has neighbours: {[nearest_vertex.name for nearest_vertex in graph.vertices[vertex].nearest_vertices]}')
