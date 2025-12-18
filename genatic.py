import random
 
def genetic_algorithm(start, goal, moves, valid, heuristic, generations=100):
    population = [[start] for _ in range(10)]


    def fitness(path):
        return 1 / (len(path) + heuristic(path[-1], goal))


    for _ in range(generations):
         population.sort(key=fitness, reverse=True)
         new_population = population[:2]


         while len(new_population) < 10:
            parent = random.choice(population[:5])
            child = parent[:]
            dx, dy = random.choice(moves)
            x, y = child[-1][0] + dx, child[-1][1] + dy
            if valid(x, y):
                child.append((x, y))
            new_population.append(child)
         population = new_population


    best = max(population, key=fitness)
    return best