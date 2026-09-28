rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []
entrance = None

print("Enter the parking grid:")

for i in range(rows):
    row = input().split()
    grid.append(row)

    for j in range(cols):
        if row[j] == "E":
            entrance = (i, j)

queue = []
queue.append(entrance)

visited = []
visited.append(entrance)

parent = {}
target = None

while len(queue) > 0:

    curr = queue.pop(0)
    x = curr[0]
    y = curr[1]

    if grid[x][y] == "A":
        target = curr
        break

    # Move Up
    if x - 1 >= 0:
        if (x - 1, y) not in visited:
            if grid[x - 1][y] == "R" or grid[x - 1][y] == "A":
                visited.append((x - 1, y))
                parent[(x - 1, y)] = curr
                queue.append((x - 1, y))

    # Move Down
    if x + 1 < rows:
        if (x + 1, y) not in visited:
            if grid[x + 1][y] == "R" or grid[x + 1][y] == "A":
                visited.append((x + 1, y))
                parent[(x + 1, y)] = curr
                queue.append((x + 1, y))

    # Move Left
    if y - 1 >= 0:
        if (x, y - 1) not in visited:
            if grid[x][y - 1] == "R" or grid[x][y - 1] == "A":
                visited.append((x, y - 1))
                parent[(x, y - 1)] = curr
                queue.append((x, y - 1))

    # Move Right
    if y + 1 < cols:
        if (x, y + 1) not in visited:
            if grid[x][y + 1] == "R" or grid[x][y + 1] == "A":
                visited.append((x, y + 1))
                parent[(x, y + 1)] = curr
                queue.append((x, y + 1))

if target is None:
    print("No reachable parking space found.")

else:
    path = []

    while target != entrance:
        path.append(target)
        target = parent[target]

    path.append(entrance)
    path.reverse()

    print("Nearest available parking space:", path[-1])
    print("Minimum movements required:", len(path) - 1)

    print("Route:")
    for p in path:
        print(p)