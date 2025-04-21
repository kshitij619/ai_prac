from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

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

path = bfs(graph, 'A', 'E')
print("Path from A to E:", path)