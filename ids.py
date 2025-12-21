def dfs_limited(node, goal, valid, moves, depth, path, visited, expanded_nodes, max_space):
    expanded_nodes[0] += 1
    max_space[0] = max(max_space[0], len(path) + len(visited))

    if node == goal:
        return path

    if depth == 0:
        return None

    x, y = node
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        neighbor = (nx, ny)
        if valid(nx, ny) and neighbor not in visited:
            visited.add(neighbor)
            result = dfs_limited(neighbor, goal, valid, moves, depth-1, path + [neighbor], visited, expanded_nodes, max_space)
            if result is not None:
                return result
            visited.remove(neighbor)  # backtrack
    return None

def ids(grid, start, goal, valid, moves, max_depth=50):
    expanded_nodes = [0]
    max_space = [0]

    for depth in range(max_depth):
        visited = set()
        visited.add(start)
        path = dfs_limited(start, goal, valid, moves, depth, [start], visited, expanded_nodes, max_space)
        if path is not None:
            return path, expanded_nodes[0], max_space[0]

    return None, expanded_nodes[0], max_space[0]
