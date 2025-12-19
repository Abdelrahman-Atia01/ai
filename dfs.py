def dfs(grid, start, goal, valid, moves):
    stack = [(start, [start])]
    visited = {start}

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        for dx, dy in moves:
            nx, ny = node[0] + dx, node[1] + dy
            if valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))

