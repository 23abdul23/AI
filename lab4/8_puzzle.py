import heapq

print("Enter initial state:")
start = []
for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)

print("Enter goal state:")
goal = []
for i in range(3):
    row = list(map(int, input().split()))
    goal.append(row)

depth_limit = int(input("Enter depth limit: "))
nodes_generated = 0

def bfs(start, goal):
    global nodes_generated
    queue = [(start, [start])]
    visited = {tuple(map(tuple, start))}

    while queue:
        current, path = queue.pop(0)

        if current == goal:
            return path

        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    r, c = i, j

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [row[:] for row in current]
                new_state[r][c], new_state[nr][nc] = \
                    new_state[nr][nc], new_state[r][c]

                nodes_generated += 1
                key = tuple(map(tuple, new_state))

                if key not in visited:
                    visited.add(key)
                    queue.append(
                        (new_state, path + [new_state])
                    )
    return None


def dfs(start, goal):
    global nodes_generated
    visited = set()

    def search(current, path, depth):
        if current == goal:
            return path

        if depth == depth_limit:
            return None

        key = tuple(map(tuple, current))
        visited.add(key)

        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    r, c = i, j

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [row[:] for row in current]
                new_state[r][c], new_state[nr][nc] = \
                    new_state[nr][nc], new_state[r][c]

                nodes_generated += 1
                new_key = tuple(map(tuple, new_state))

                if new_key not in visited:
                    result = search(
                        new_state,
                        path + [new_state],
                        depth + 1
                    )

                    if result is not None:
                        return result

        return None
    return search(start, [start], 0)



def a_star(start, goal):
    global nodes_generated

    h = 0
    for i in range(3):
        for j in range(3):
            if start[i][j] != 0 and start[i][j] != goal[i][j]:
                h += 1

    heap = [(h, 0, start, [start])]
    visited = set()

    while heap:
        f, g, current, path = heapq.heappop(heap)
        key = tuple(map(tuple, current))

        if key in visited:
            continue

        visited.add(key)

        if current == goal:
            return path
        
        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    r, c = i, j

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [row[:] for row in current]

                new_state[r][c], new_state[nr][nc] = \
                    new_state[nr][nc], new_state[r][c]

                nodes_generated += 1
                new_key = tuple(map(tuple, new_state))

                if new_key in visited:
                    continue

                new_g = g + 1
                new_h = 0

                for i in range(3):
                    for j in range(3):
                        if (new_state[i][j] != 0 and
                            new_state[i][j] != goal[i][j]):
                            new_h += 1

                new_f = new_g + new_h
                heapq.heappush(
                    heap,
                    (
                        new_f,
                        new_g,
                        new_state,
                        path + [new_state]
                    )
                )

    return None

for name, function in [
    ("BFS", bfs),
    ("DFS", dfs),
    ("A*", a_star)
]:

    nodes_generated = 0
    solution = function(start, goal)

    print("\n====================")
    print(name)
    print("====================")

    if solution is None:
        print("No solution found.")

    else:
        print("Solution depth:", len(solution) - 1)
        print("Nodes generated:", nodes_generated)

        for step, state in enumerate(solution):
            print("\nStep", step)

            for row in state:
                print(
                    " ".join(
                        "#" if x == 0 else str(x)
                        for x in row
                    )
                )