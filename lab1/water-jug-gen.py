from collections import deque


def water_jug_solver(capacity1, capacity2, start, goal):

    queue = deque([start])
    visited = {start}

    parent = {start: None}
    action = {}

    while queue:

        current = queue.popleft()
        x, y = current

        # Goal reached
        if current == goal:
            break

        # Generate all possible states
        next_states = []

        # 1. Fill Jug 1
        next_states.append(
            ((capacity1, y), "Fill Jug 1")
        )

        # 2. Fill Jug 2
        next_states.append(
            ((x, capacity2), "Fill Jug 2")
        )

        # 3. Empty Jug 1
        next_states.append(
            ((0, y), "Empty Jug 1")
        )

        # 4. Empty Jug 2
        next_states.append(
            ((x, 0), "Empty Jug 2")
        )

        # 5. Pour Jug 1 -> Jug 2
        amount = min(x, capacity2 - y)

        next_states.append(
            (
                (x - amount, y + amount),
                "Pour Jug 1 -> Jug 2"
            )
        )

        # 6. Pour Jug 2 -> Jug 1
        amount = min(y, capacity1 - x)

        next_states.append(
            (
                (x + amount, y - amount),
                "Pour Jug 2 -> Jug 1"
            )
        )

        # Add unvisited states
        for new_state, operation in next_states:

            if new_state not in visited:

                visited.add(new_state)
                queue.append(new_state)

                parent[new_state] = current
                action[new_state] = operation

    # Goal is unreachable
    if goal not in visited:
        print("No solution exists.")
        return

    # Reconstruct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    # Print solution
    print(f"Start State: {start}")

    for i in range(1, len(path)):
        state = path[i]
        print(f"{action[state]:<25}: {state}")

    print(f"Goal State: {goal}")


water_jug_solver(
    4,          # Capacity of Jug 1
    3,          # Capacity of Jug 2
    (0, 0),     # Start state
    (2, 0)      # Goal state
)

# Example test: run the file directly.
# Expected: a sequence of fill, pour, and empty actions ending at Goal State: (2, 0).