from collections import deque
import graph as g


graph = g.Graph()
graph = g.populate_graph(graph, g.example_graph2)

def bf_traversal(tree):
    '''Breadth-first tree traaversal with loops'''
    queue = deque()
    queue += [tree.root]
    traversed = []
    contents = []
    while queue:
        current_node = queue.popleft()
        if current_node.name not in traversed:
            contents.append((current_node.name, current_node.content))
        traversed.append(current_node.name)
        for adjacent_node in current_node.nearest_vertices:
            if adjacent_node.name not in traversed:
                queue.append(adjacent_node)
                contents.append((adjacent_node.name, adjacent_node.content))
                traversed.append(adjacent_node.name)
    return contents



def df_traversal(tree):
    '''Depth-first tree traversal with recursion'''
    traversed = []
    contents = []

    def df_traversal_recursive(node):
        if node.name not in traversed:
            contents.append((node.name, node.content))
            traversed.append(node.name)
        if node.nearest_vertices:
            for subnode in node.nearest_vertices:
                df_traversal_recursive(subnode)

    df_traversal_recursive(tree.root)
    return contents

print(bf_traversal(graph))
print(df_traversal(graph))
