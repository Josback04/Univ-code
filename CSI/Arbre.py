G= {
    'A': ['B', 'C'],
    'B': ['C', 'A'],
    'C': ['B','A','D'],
    'D': ['C', 'F'],
    'F': ['D']


}

def parcours_en_profondeur(graph, node, visited=None):
    if visited is None:
        visited=[]
    if node is not visited:
        visited.append(node)

    unvisited=[n for n in graph[node] if n not in visited ]
    for node in unvisited:
        parcours_en_profondeur(graph, node, visited)
    return visited

print(parcours_en_profondeur(G,'F'))