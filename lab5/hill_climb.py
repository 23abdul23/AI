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

    # Warehouse to first location
    total += distance("W", route[0])

    # Distance between delivery locations
    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])

    # Last location back to warehouse
    total += distance(route[-1], "W")

    return total


def hill_climbing():
    current_route = delivery_locations.copy()
    random.shuffle(current_route)

    current_cost = route_cost(current_route)

    print("Initial Route:")
    print("W ->", " -> ".join(current_route), "-> W")
    print("Initial Cost:", round(current_cost, 2))
    print()

    iteration = 0

    while True:
        best_route = current_route.copy()
        best_cost = current_cost

        # Generate all 21 swap neighbours
        for i in range(len(current_route)):
            for j in range(i + 1, len(current_route)):

                neighbour = current_route.copy()

                neighbour[i], neighbour[j] = neighbour[j], neighbour[i]

                cost = route_cost(neighbour)

                if cost < best_cost:
                    best_cost = cost
                    best_route = neighbour

        # No better neighbour found
        if best_cost >= current_cost:
            break

        current_route = best_route
        current_cost = best_cost

        iteration += 1

        print("Iteration", iteration)
        print("Best Route:",
              "W ->", " -> ".join(current_route), "-> W")
        print("Cost:", round(current_cost, 2))
        print()

    print("Final Route:")
    print("W ->", " -> ".join(current_route), "-> W")
    print("Final Cost:", round(current_cost, 2))
    print("Number of Iterations:", iteration)

    return current_cost, iteration


hill_climbing()