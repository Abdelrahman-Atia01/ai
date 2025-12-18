import heapq


def manhattan_distance(a, b):
    """
    Heuristic function (Manhattan Distance)
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal, valid, moves):
    """
    A* Search Algorithm
    Returns the path from start to goal if exists
    """

    # open list as priority queue: (f, node, path, g)
    open_list = []
    heapq.heappush(open_list, (0, start, [start], 0))

    visited = set()

    while open_list:
        f, node, path, g = heapq.heappop(open_list)

        # Goal check
        if node == goal:
            return path

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

    return None