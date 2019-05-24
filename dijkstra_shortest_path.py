import weighted_graph as wg 
import numpy as np


graph = wg.populate_weighted_graph(wg.letters, wg.edges, wg.weights)

def find_shortest_path(graph, start, end):
    if isinstance(graph, wg.WeightedGraph):
        if start in graph.vertices.keys() and end in graph.vertices.keys():
            shortest_path_to = dict([(node, ('', np.inf)) for node in graph.vertices.keys()])
            finished_nodes = []
            remaining_nodes = list(graph.vertices.keys())
            shortest_path_to[start] = [start, 0]
            nodes_to_visit = [start]
            while remaining_nodes and nodes_to_visit:
                for current in nodes_to_visit.copy():
                    priority_nodes = [(node.name, shortest_path_to[node.name][1]) for node in graph.vertices[current].nearest_vertices]
                    priority_nodes = sorted(priority_nodes, key=lambda x: x[1])
                    for nearest_node in priority_nodes:
                        if shortest_path_to[current][1] + graph.edges.get(current + nearest_node[0]) < shortest_path_to[nearest_node[0]][1]:
                            shortest_path_to[nearest_node[0]] = (
                                shortest_path_to[current][0] + f'->{nearest_node[0]}',
                                shortest_path_to[current][1] + graph.edges.get(current + nearest_node[0])
                            )
                    finished_nodes.append(current)
                    remaining_nodes.remove(current)
                    nodes_to_visit.remove(current)
                    nodes_to_add = [node[0] for node in priority_nodes if node[0] not in finished_nodes and node[0] not in nodes_to_visit]
                    nodes_to_visit += nodes_to_add
            if shortest_path_to[end][1] == np.inf and shortest_path_to[end][0] == '':
                return f'Path from {start} to {end} does not exist'
            else:
                return f'Shortest path from {start} to {end} is {shortest_path_to[end][0]} with weight {shortest_path_to[end][1]}'
        elif start not in graph.vertices.keys():
            return f'Graph does not have {start} node'
        elif end not in graph.vertices.keys():
            return f'Graph does not have {end} node'
    else:
        return 'Invalid graph'

print(find_shortest_path(graph, 'A', 'F'))
print(find_shortest_path(graph, 'F', 'D'))
print(find_shortest_path(graph, 'G', 'F'))


graph2 = wg.populate_weighted_graph('ABCDEF', 'AB AC AD AE BD BE BF CB CD CE CF DE DF EF'.split(' '), [6, 8, 11, 10, 9, 7, 15, 8, 7, 4, 11, 6, 7, 9])
print(find_shortest_path(graph2, 'A', 'F'))
