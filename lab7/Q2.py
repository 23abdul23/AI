import random

# Q2: 0/1 Knapsack using Genetic Algorithm
# Capacity = 15 kg
# A: weight 7, value 500
# B: weight 2, value 400
# C: weight 1, value 700
# D: weight 9, value 200

weights = [7, 2, 1, 9]
values = [500, 400, 700, 200]
names = ["A", "B", "C", "D"]

CAPACITY = 15
POP_SIZE = 8
GENERATIONS = 25
MUTATION_RATE = 0.05

def fitness(chromosome):
    total_weight = sum(int(chromosome[i]) * weights[i] for i in range(4))
    total_value = sum(int(chromosome[i]) * values[i] for i in range(4))

    if total_weight > CAPACITY:
        return 0
    return total_value

def total_weight(chromosome):
    return sum(int(chromosome[i]) * weights[i] for i in range(4))

def random_chromosome():
    return "".join(random.choice("01") for _ in range(4))

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
        f"Best = {best}, "
        f"Weight = {total_weight(best)} kg, "
        f"Fitness = Rs. {fitness(best)}"
    )

    # Elitism
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

selected_items = [names[i] for i in range(4) if best[i] == "1"]

print("\nFinal Result")
print("Best chromosome:", best)
print("Selected items:", selected_items)
print("Total weight:", total_weight(best), "kg")
print("Maximum value found: Rs.", fitness(best))

# Exact optimum is chromosome 1110:
# A + B + C => weight = 10 kg, value = Rs. 1600.
