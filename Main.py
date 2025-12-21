import time
from bfs import bfs
from dfs import dfs
from ucs import ucs
from ids import ids
from astar import astar
from genetic import genetic_algorithm

# Grid
grid = [
    ['S', 0, 0, 1, 0],
    [1,   1, 0, 1, 0],
    [0,   0, 0, 0, 0],
    [0,   1, 1, 1, 0],
    [0,   0, 0, 'G', 0]
]

ROWS = len(grid)
COLS = len(grid[0])

def find_position(val):
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == val:
                return (i, j)

start = find_position('S')
goal = find_position('G')

moves = [(0,1),(1,0),(0,-1),(-1,0)]

def valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] != 1

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def run_algorithm(name, func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()

    if result is None:
        path, expanded, space = None, None, None
    else:
        path, expanded, space = result

    path_cost = len(path) - 1 if path else None

    print(f"\n{name}")
    print("Path:", path)
    print("Path Cost:", path_cost)
    print("Nodes Explored:", expanded)
    print("Space Usage:", space)
    print("Execution Time (ms):", round((end_time - start_time)*1000, 3))

    return path_cost

# Run algorithms
costs = {}

costs["BFS"] = run_algorithm("BFS", bfs, grid, start, goal, valid, moves)
costs["DFS"] = run_algorithm("DFS", dfs, grid, start, goal, valid, moves)
costs["UCS"] = run_algorithm("UCS", ucs, grid, start, goal, valid, moves)
costs["IDS"] = run_algorithm("IDS", ids, grid, start, goal, valid, moves)
costs["A*"]  = run_algorithm("A*", astar, grid, start, goal, valid, moves)

# Genetic Algorithm (no guarantees)
start_time = time.time()
path_gen = genetic_algorithm(start, goal, moves, valid, heuristic)
end_time = time.time()

print("\nGenetic Algorithm")
print("Path:", path_gen)
print("Execution Time (ms):", round((end_time - start_time)*1000, 3))






 



