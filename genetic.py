import random

def genetic_algorithm(start, goal, moves, valid, heuristic, generations=100, pop_size=10):
    population = [[start] for _ in range(pop_size)]

    expanded_nodes = 0
    max_space = len(population)

    def fitness(path):
        return 1 / (len(path) + heuristic(path[-1], goal))

    for _ in range(generations):
        expanded_nodes += len(population)
        max_space = max(max_space, len(population))

        population.sort(key=fitness, reverse=True)
        new_population = population[:2]   

        while len(new_population) < pop_size:
     
            parent1 = random.choice(population[:5])
            parent2 = random.choice(population[:5])

            if len(parent1) > 1 and len(parent2) > 1:
                cut = random.randint(1, min(len(parent1), len(parent2)) - 1)
                child = parent1[:cut] + parent2[cut:]
            else:
                child = parent1[:]

   
            dx, dy = random.choice(moves)
            x, y = child[-1][0] + dx, child[-1][1] + dy
            if valid(x, y):
                child.append((x, y))

            new_population.append(child)

        population = new_population

        for p in population:
            if p[-1] == goal:
                return p, expanded_nodes, max_space

    best = max(population, key=fitness)
    if best[-1] == goal:
        return best, expanded_nodes, max_space
    else:
        return [start], expanded_nodes, max_space
        

