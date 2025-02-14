"""

"""
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs_recursive(graph, neighbor, visited)
            
# Breaking it Down
# 1. graph.get(node, [])

#     graph is a dictionary representing an adjacency list of a graph.
#     graph.get(node, []):
#         Looks up the neighbors (connected nodes) of node in graph.
#         If node is not found, it returns an empty list ([]) instead of raising an error.

# 2. for neighbor in graph.get(node, [])

#     Loops through all neighbors of the current node.
#     Each neighbor represents a connected node that we will visit next in DFS.

# graph.get(node, []) ensures safe lookup of neighbors.

# for neighbor in graph.get('B', []):  # ['D', 'E']
# for neighbor in graph.get('F', []):  # []


# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform DFS from node 'A'
dfs_recursive(graph, 'A')
