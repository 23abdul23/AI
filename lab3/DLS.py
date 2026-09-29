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

def dls(state, depth, path, visited):
    global nodes_generated
    nodes_generated += 1

    if state == goal:
        return path


    if depth == depth_limit:
        return None

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x = i
                y = j

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dx, dy, move in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = []
            for row in state:
                new_state.append(row[:])

            temp = new_state[x][y]
            new_state[x][y] = new_state[nx][ny]
            new_state[nx][ny] = temp

            state_tuple = tuple(tuple(row) for row in new_state)

            if state_tuple not in visited:
                visited.add(state_tuple)
                result = dls(
                    new_state,
                    depth + 1,
                    path + [move],
                    visited
                )

                if result is not None:
                    return result
                
                visited.remove(state_tuple)

    return None

visited = set()
start_tuple = tuple(tuple(row) for row in start)
visited.add(start_tuple)

solution = dls(start, 0, [], visited)

if solution is None:
    print("Goal not found within depth limit.")
else:
    print("Goal found within depth limit.")
    print("Sequence of moves:", solution)
    print("Total moves:", len(solution))

print("Total nodes generated:", nodes_generated)

# Example test input:
# 1 2 3
# 4 0 6
# 7 5 8
# 1 2 3
# 4 5 6
# 7 8 0
# 5
# Expected: goal found within depth limit and a move sequence is printed.