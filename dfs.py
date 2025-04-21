from collections import deque

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F', 'E'],
    'C': ['G'],
    'D': ['F'],
    'F': ['E'],
    'E': ['G'],
    'G': []
}

path = dfs(graph, 'A', 'E')
print("Path from A to E:", path)