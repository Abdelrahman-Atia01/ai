
def dfs(grid, start, goal, moves):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    path = []

    def dfs_util(x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return False

        if grid[x][y] == 1 or visited[x][y]:
            return False

        visited[x][y] = True
        path.append((x, y))

        if (x, y) == goal:
            return True

        for dx, dy in moves:
            if dfs_util(x + dx, y + dy):
                return True

        path.pop()
        return False

    if dfs_util(start[0], start[1]):
        return path
    else:
        return None
