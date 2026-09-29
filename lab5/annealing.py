import random
import math

locations = {
    "W": (0, 0),
    "A": (2, 6),
    "B": (5, 2),
    "C": (6, 7),
    "D": (8, 3),
    "E": (1, 4),
    "F": (7, 6),
    "G": (3, 1)
}

delivery_locations = ["A", "B", "C", "D", "E", "F", "G"]


def distance(a, b):
    x1, y1 = locations[a]
    x2, y2 = locations[b]

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def route_cost(route):
    total = 0

    total += distance("W", route[0])

    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])

    total += distance(route[-1], "W")

    return total


def simulated_annealing():
    current_route = delivery_locations.copy()
    random.shuffle(current_route)

    current_cost = route_cost(current_route)

    best_route = current_route.copy()
    best_cost = current_cost

    temperature = 100
    cooling_rate = 0.95
    minimum_temperature = 0.1

    iteration = 0

    print("Initial Route:")
    print("W ->", " -> ".join(current_route), "-> W")
    print("Initial Cost:", round(current_cost, 2))
    print()

    while temperature >= minimum_temperature:

        neighbour = current_route.copy()

        # Select two random positions
        i, j = random.sample(range(len(neighbour)), 2)

        # Swap them
        neighbour[i], neighbour[j] = neighbour[j], neighbour[i]

        neighbour_cost = route_cost(neighbour)

        delta_e = neighbour_cost - current_cost

        accepted = False

        # Better route
        if delta_e < 0:
            accepted = True

        else:
            probability = math.exp(-delta_e / temperature)
            r = random.random()

            if r < probability:
                accepted = True

        if accepted:
            current_route = neighbour
            current_cost = neighbour_cost

            if current_cost < best_cost:
                best_cost = current_cost
                best_route = current_route.copy()

        iteration += 1

        print("Iteration:", iteration)
        print("Temperature:", round(temperature, 2))
        print("Current Cost:", round(current_cost, 2))

        if accepted:
            print("Neighbour: Accepted")
        else:
            print("Neighbour: Rejected")

        print()

        # Cool temperature
        temperature = temperature * cooling_rate

    print("Best Route Found:")
    print("W ->", " -> ".join(best_route), "-> W")
    print("Best Cost:", round(best_cost, 2))
    print("Number of Iterations:", iteration)

    return best_cost, iteration


simulated_annealing()

# Example test: run the file directly.
# Expected: a random initial route, temperature iterations, and a best route summary.