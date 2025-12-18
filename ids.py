def dfs_limited(node, goal, valid, moves, depth, path, visited):
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
            result = dfs_limited(neighbor, goal, valid, moves, depth-1, path + [neighbor], visited)
            if result is not None:
                return result
            visited.remove(neighbor)  # backtrack
    return None

def ids(grid, start, goal, valid, moves, max_depth=50):
    for depth in range(max_depth):
        visited = set()
        visited.add(start)
        path = dfs_limited(start, goal, valid, moves, depth, [start], visited)
        if path is not None:
            return path
    return None