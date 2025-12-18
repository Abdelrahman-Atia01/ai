from bfs import bfs
from genatic import genetic_algorithm
from Ucs import ucs
from dfs import dfs
from ids import ids
from astar import astar

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


# Run BFS
path = bfs(grid, start, goal, valid, moves)
print("BFS Path:", path)

#Run DFS
path_dfs = dfs(grid, start, goal, moves)
print("DFS Path:", path_dfs)


#Run UCS
path_ucs=ucs(grid,start,goal,valid,moves)
print("UCS Algorithm Path:",path_ucs)

#Run IDS
path_ids = ids(grid, start, goal, valid, moves)
print("IDS Path:", path_ids)

#Run A*
path_astar=astar(grid, start, goal, valid, moves)
print("A* Algorithm:",path_astar)

# Run Genetic Algorithm
path_gen = genetic_algorithm(start, goal, moves, valid, heuristic)
print("Genetic Algorithm Path:", path_gen)






 

