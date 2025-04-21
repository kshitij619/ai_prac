import heapq

# Define the goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank space

# Heuristic: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Check if a state is the goal
def is_goal(state):
    return state == GOAL_STATE

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert state to a tuple of tuples for hashing
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Algorithm
def a_star(start_state):
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if is_goal(current):
            return path + [current]

        visited.add(state_to_tuple(current))

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                heapq.heappush(open_list, (
                    g + 1 + manhattan_distance(neighbor),
                    g + 1,
                    neighbor,
                    path + [current]
                ))

    return None  # No solution

# Example usage
if __name__ == "__main__":
    start = [[1, 2, 3],
             [5, 0, 6],
             [4, 7, 8]]  # Replace with your initial state

    solution = a_star(start)

    if solution:
        print("Solution found in", len(solution) - 1, "moves:")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")

