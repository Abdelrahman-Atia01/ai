import heapq

def manhattan_distance(a, b):
    """Heuristic function (Manhattan Distance)"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal, valid, moves):
    """
    A* Search Algorithm
    Returns the path, nodes expanded, and peak space usage
    """

    # open list as priority queue: (f, node, path, g)
    open_list = []
    heapq.heappush(open_list, (0, start, [start], 0))

    visited = set()
    expanded_nodes = 0
    max_space = len(open_list) + len(visited)

    while open_list:
        f, node, path, g = heapq.heappop(open_list)
        expanded_nodes += 1
        max_space = max(max_space, len(open_list) + len(visited))

        # Goal check
        if node == goal:
            return path, expanded_nodes, max_space

        if node in visited:
            continue

        visited.add(node)

        # Explore neighbors
        for dx, dy in moves:
            nx, ny = node[0] + dx, node[1] + dy
            neighbor = (nx, ny)

            if valid(nx, ny) and neighbor not in visited:
                new_g = g + 1
                h = manhattan_distance(neighbor, goal)
                new_f = new_g + h
                heapq.heappush(
                    open_list,
                    (new_f, neighbor, path + [neighbor], new_g)
                )

    return None, expanded_nodes, max_space
