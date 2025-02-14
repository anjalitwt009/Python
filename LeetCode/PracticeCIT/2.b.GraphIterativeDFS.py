def dfs_iterative(graph, start):
    stack = [start]  # Stack to keep track of nodes to visit
    visited = set()  # Set to track visited nodes

    while stack:
        node = stack.pop()  # Get the last element from stack
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark node as visited
            stack.extend(graph.get(node, []))  # Add neighbors to stack

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
dfs_iterative(graph, 'A')
