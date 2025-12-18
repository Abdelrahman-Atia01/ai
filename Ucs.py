import heapq

def ucs(grid, start, goal, valid, moves):
    # priority queue: (cost, node, path)
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for dx, dy in moves:
            nx, ny = node[0] + dx, node[1] + dy
            next_node = (nx, ny)

            if valid(nx, ny) and next_node not in visited:
                # cost of each move = 1
                heapq.heappush(
                    pq,
                    (cost + 1, next_node, path + [next_node])
                )

    return None, float("inf")