# Assignment-1: Maze Solver using BFS and DFS

# Objective: Implement BFS and DFS to solve a maze.
# Problem Statement: Given a grid-based maze where 0 represents walls and 1
# represents walkable paths, find the shortest path from a start cell to an end cell.
# Tasks:
#  Use BFS to find the shortest path.
#  Use DFS to explore all possible paths and report one valid path (not necessarily
# the shortest).
#  Compare the number of nodes explored by BFS and DFS.
from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1
        if current == end:
            path = reconstruct_path(parent, start, end)
            return path, nodes_explored

        for neighbor in get_neighbors(maze, current, rows, cols):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None, nodes_explored  

def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    visited.add(start)
    path = []
    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1
        path.append(current)
        if current == end:
            return path, nodes_explored

        for neighbor in get_neighbors(maze, current, rows, cols):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return None, nodes_explored  

def get_neighbors(maze, cell, rows, cols):
    x, y = cell
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
            neighbors.append((nx, ny))
    return neighbors

def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = parent[current]
    return path[::-1]

def validate_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    sx, sy = start
    ex, ey = end
    if not (0 <= sx < rows and 0 <= sy < cols): 
        return "Start point is out of bounds!"
    if not (0 <= ex < rows and 0 <= ey < cols): 
        return "End point is out of bounds!"
    if maze[sx][sy] == 0:
        return "Start point is a wall!"  
    if maze[ex][ey] == 0:
        return "End point is a wall!" 
    return None

def simulate_agent(path):
    actions = []
    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]
        if x2 == x1 and y2 == y1 + 1:
            actions.append("Move Right")
        elif x2 == x1 and y2 == y1 - 1:
            actions.append("Move Left")
        elif x2 == x1 + 1 and y2 == y1:
            actions.append("Move Down")
        elif x2 == x1 - 1 and y2 == y1:
            actions.append("Move Up")
    return actions

def input_grid():
    print("Enter the maze grid row by row (0 for walls, 1 for paths) :") #Separate rows by pressing Enter and terminate input with an empty line.
    maze = []
    while True:
        line = input()
        if line.strip() == "":
            break
        maze.append(list(map(int, line.split())))
    return maze

def main():
    maze = input_grid()
    print("\nInput the start and end coordinates in the format: x y")
    x_start, y_start = map(int, input("Start cell: ").split())
    x_end, y_end = map(int, input("End cell: ").split())
    start = (x_start, y_start)
    end = (x_end, y_end)
    validation_error = validate_maze(maze, start, end)
    if validation_error:
        print(f"Error: {validation_error}")
        return
    
    bfs_path, bfs_nodes = bfs(maze, start, end)
    dfs_path, dfs_nodes = dfs(maze, start, end)
    bfs_actions = simulate_agent(bfs_path) if bfs_path else []
    dfs_actions = simulate_agent(dfs_path) if dfs_path else []

    print("\nResults:")
    print("BFS Path:", bfs_path if bfs_path else "No path found")
    print("BFS Nodes Explored:", bfs_nodes)
    print("BFS Actions:", bfs_actions)

    print("\nDFS Path:", dfs_path if dfs_path else "No path found")
    print("DFS Nodes Explored:", dfs_nodes)
    print("DFS Actions:", dfs_actions)

if __name__ == "__main__":
    main()
