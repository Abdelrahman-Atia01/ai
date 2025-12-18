from collections import deque

def bfs(grid, start, goal, valid, moves):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for dx, dy in moves:
            nx, ny = node[0]+dx, node[1]+dy
            if valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path+[(nx, ny)]))
