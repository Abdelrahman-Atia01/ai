import heapq

def ucs(grid, start, goal, valid, moves):
    """
    Uniform Cost Search
    Returns: path, nodes expanded, peak space usage
    """
    pq = [(0, start, [start])]
    visited = set()

    expanded_nodes = 0
    max_space = len(pq) + len(visited)

    while pq:
        cost, node, path = heapq.heappop(pq)
        expanded_nodes += 1
        max_space = max(max_space, len(pq) + len(visited))

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, expanded_nodes, max_space

        for dx, dy in moves:
            nx, ny = node[0] + dx, node[1] + dy
            next_node = (nx, ny)
            if valid(nx, ny) and next_node not in visited:
                # cost of each move = 1
                heapq.heappush(pq, (cost + 1, next_node, path + [next_node]))

    return None, expanded_nodes, max_space



    return None, float("inf")
