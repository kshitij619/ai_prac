from heapq import heappush, heappop

def astar(graph, start, goal):
    open_set = []
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    came_from = {}
    
    heappush(open_set, (g_score[start] + graph[start]['h'], start))
    
    while open_set:
        current_f, current = heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]
        
        for neighbor, cost in graph[current]['edges'].items():
            tentative_g = g_score[current] + cost
            
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + graph[neighbor]['h']
                heappush(open_set, (f_score, neighbor))
    
    return None, None

graph = {
    'S': {'h': 7, 'edges': {'A': 4, 'B': 10, 'C': 11}},
    'A': {'h': 8, 'edges': {'B': 8, 'D': 5}},
    'B': {'h': 6, 'edges': {'D': 15, 'C': 8}},
    'C': {'h': 5, 'edges': {'E': 20, 'F': 2}},
    'D': {'h': 5, 'edges': {'H': 16, 'I': 1, 'F': 1}},

   
    'E': {'h': 3, 'edges': {'G': 19}},
    'F': {'h': 3, 'edges': {'G': 13}},
    'G': {'h': 0, 'edges': {}},
    'H': {'h': 7, 'edges': {'I': 1, 'J': 2}},
    'I': {'h': 4, 'edges': {'J': 5, 'K': 13, 'G': 5}},
    'J': {'h': 5, 'edges': {'K': 7}},
    'K': {'h': 3, 'edges': {'G': 16}}
}

path, cost = astar(graph, 'S', 'G')
print(f"Path: {' -> '.join(path)}")
print(f"Total cost: {cost}")
