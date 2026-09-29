import heapq

graph = {
    'a': {'b': 5, 'c': 2, 'd': 3},
    'b': {'a': 5, 'c': 2, 'f': 3},
    'c': {'a': 2, 'b': 2, 'd': 1, 'e': 2, 'f': 6},
    'd': {'a': 3, 'c': 1, 'e': 4},
    'e': {'c': 2, 'd': 4, 'f': 4},
    'f': {'b': 3, 'c': 6, 'e': 4}
}

heuristic = {
    'a': 6,
    'b': 2,
    'c': 5,
    'd': 6,
    'e': 4,
    'f': 0
}

def dijkstra(graph, start, goal):
    queue = [(0, start)]

    distance = {
        start: 0
    }

    parent = {
        start: None
    }

    visited = set()
    while queue:
        cost, current = heapq.heappop(queue)
        if current in visited:
            continue

        visited.add(current)
        if current == goal:
            break

        for neighbour in graph[current]:
            new_cost = cost + graph[current][neighbour]
            if new_cost < distance.get(neighbour, float('inf')):
                distance[neighbour] = new_cost
                parent[neighbour] = current

                heapq.heappush(
                    queue,
                    (new_cost, neighbour)
                )

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path, distance[goal]


def a_star(graph, start, goal, heuristic):

    queue = [
        (heuristic[start], 0, start)
    ]

    g_cost = {
        start: 0
    }

    parent = {
        start: None
    }

    visited = set()
    while queue:
        f, cost, current = heapq.heappop(queue)
        if current in visited:
            continue

        visited.add(current)
        if current == goal:
            break

        for neighbour in graph[current]:
            new_cost = cost + graph[current][neighbour]
            if new_cost < g_cost.get(
                neighbour,
                float('inf')
            ):

                g_cost[neighbour] = new_cost
                parent[neighbour] = current
                new_f = new_cost + heuristic[neighbour]

                heapq.heappush(
                    queue,
                    (new_f, new_cost, neighbour)
                )

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path, g_cost[goal]



path, cost = dijkstra(graph, 'a', 'f')

print("\n====================")
print("Dijkstra's Algorithm")
print("====================")

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)

# Example test: run the file directly.
# Expected: Dijkstra and A* both print a shortest path from a to f and its cost.


path, cost = a_star(
    graph,
    'a',
    'f',
    heuristic
)

print("\n====================")
print("A* Algorithm")
print("====================")

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)