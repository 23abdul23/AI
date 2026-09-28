n = int(input("Enter number of nodes: "))

city_map = {}
print("Enter node names:")
nodes = input().split()

for node in nodes:
    city_map[node] = []

edges = int(input("Enter number of edges: "))
print("Enter edges:")

for i in range(edges):
    u, v = input().split()
    city_map[u].append(v)
    city_map[v].append(u)

source = input("Enter source: ")
goal = input("Enter goal: ")

# BFS from source
queue1 = []
queue1.append(source)

visited1 = []
visited1.append(source)

parent1 = {}
parent1[source] = None

# BFS from goal
queue2 = []
queue2.append(goal)

visited2 = []
visited2.append(goal)

parent2 = {}
parent2[goal] = None

meeting_point = None

while len(queue1) > 0 and len(queue2) > 0:

    curr = queue1.pop(0)

    for neighbour in city_map[curr]:
        if neighbour not in visited1:
            visited1.append(neighbour)
            parent1[neighbour] = curr
            queue1.append(neighbour)

            if neighbour in visited2:
                meeting_point = neighbour
                break

    if meeting_point is not None:
        break

    curr = queue2.pop(0)

    for neighbour in city_map[curr]:
        if neighbour not in visited2:
            visited2.append(neighbour)
            parent2[neighbour] = curr
            queue2.append(neighbour)

            if neighbour in visited1:
                meeting_point = neighbour
                break

    if meeting_point is not None:
        break

if meeting_point is None:
    print("No connecting path exists.")

else:
    path1 = []
    curr = meeting_point

    while curr is not None:
        path1.append(curr)
        curr = parent1[curr]

    path1.reverse()

    path2 = []
    curr = parent2[meeting_point]

    while curr is not None:
        path2.append(curr)
        curr = parent2[curr]

    path = path1 + path2

    print("Path:", " -> ".join(path))
    print("Meeting point:", meeting_point)
    print("Nodes visited from source:", visited1)
    print("Nodes visited from goal:", visited2)