import random

def genetic_algorithm(start, goal, moves, valid, heuristic, generations=100, pop_size=10):
    population = [[start] for _ in range(pop_size)]

    expanded_nodes = 0
    max_space = len(population)

    def fitness(path):
        return 1 / (len(path) + heuristic(path[-1], goal))

    for _ in range(generations):
        # عد كل Path كـ Nodes Expanded
        expanded_nodes += len(population)
        max_space = max(max_space, len(population))

        population.sort(key=fitness, reverse=True)
        new_population = population[:2]

        while len(new_population) < pop_size:
            parent = random.choice(population[:5])
            child = parent[:]
            dx, dy = random.choice(moves)
            x, y = child[-1][0] + dx, child[-1][1] + dy
            if valid(x, y):
                child.append((x, y))
            new_population.append(child)
        population = new_population

        # تحقق إذا أي Path وصل Goal
        for p in population:
            if p[-1] == goal:
                return p, expanded_nodes, max_space

    # لو محدش وصل Goal، نرجع أفضل Path حتى آخر جيل
    best = max(population, key=fitness)
    if best[-1] == goal:
        return best, expanded_nodes, max_space
    else:
        return [start], expanded_nodes, max_space  # لا حل
