import random

# Q1: Maximize f(x) = 15x - x^2, 0 <= x <= 15 using Genetic Algorithm

POP_SIZE = 8
GENERATIONS = 20
MUTATION_RATE = 0.05

def fitness(chromosome):
    x = int(chromosome, 2)
    return max(0, 15 * x - x * x)

def random_chromosome():
    return format(random.randint(0, 15), "04b")

def roulette_selection(population):
    fits = [fitness(c) for c in population]
    total = sum(fits)

    if total == 0:
        return random.choice(population)

    r = random.uniform(0, total)
    s = 0
    for c, f in zip(population, fits):
        s += f
        if s >= r:
            return c
    return population[-1]

def crossover(p1, p2):
    point = random.randint(1, 3)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

def mutate(chromosome):
    bits = list(chromosome)
    for i in range(4):
        if random.random() < MUTATION_RATE:
            bits[i] = "1" if bits[i] == "0" else "0"
    return "".join(bits)

population = [random_chromosome() for _ in range(POP_SIZE)]

for generation in range(GENERATIONS):
    population.sort(key=fitness, reverse=True)
    best = population[0]
    print(
        f"Generation {generation + 1:2d}: "
        f"Best chromosome = {best}, "
        f"x = {int(best, 2)}, "
        f"fitness = {fitness(best)}"
    )

    # Elitism: keep the best chromosome
    new_population = [best]

    while len(new_population) < POP_SIZE:
        p1 = roulette_selection(population)
        p2 = roulette_selection(population)
        c1, c2 = crossover(p1, p2)
        new_population.append(mutate(c1))
        if len(new_population) < POP_SIZE:
            new_population.append(mutate(c2))

    population = new_population

best = max(population, key=fitness)
x = int(best, 2)

print("\nFinal Result")
print("Best chromosome:", best)
print("x =", x)
print("Maximum fitness found =", fitness(best))

# Exact maximum over integer x in [0, 15] is 56 at x = 7 or x = 8.

# Example test: run the file directly.
# Expected: 20 generations and a final chromosome with fitness near or equal to 56.
