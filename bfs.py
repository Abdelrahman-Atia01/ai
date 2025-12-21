from collections import deque

def bfs(grid, start, goal, valid, moves):
    queue = deque([(start, [start])])
    visited = {start}

    expanded_nodes = 0
    max_space = len(queue) + len(visited)

    while queue:
        node, path = queue.popleft()
        expanded_nodes += 1

        max_space = max(max_space, len(queue) + len(visited))

        if node == goal:
            return path, expanded_nodes, max_space

        for dx, dy in moves:
            nx, ny = node[0] + dx, node[1] + dy
            if valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None, expanded_nodes, max_space
