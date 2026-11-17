
def initial_state():
    state = {"HANDEMPTY"}

    for b in ["w", "x", "y", "z"]:
        state.add(f"ONTABLE({b})")
        state.add(f"CLEAR({b})")

    return state


def preconditions(action):
    op, x, *rest = action

    if op == "PICKUP":
        return [
            f"ONTABLE({x})",
            f"CLEAR({x})",
            "HANDEMPTY"
        ]

    if op == "STACK":
        y = rest[0]
        return [f"HOLDING({x})", f"CLEAR({y})"]


def effects(action):
    op, x, *rest = action

    if op == "PICKUP":
        return (
            {f"HOLDING({x})"},
            {f"ONTABLE({x})", f"CLEAR({x})", "HANDEMPTY"}
        )

    if op == "STACK":
        y = rest[0]
        return (
            {f"ON({x},{y})", f"CLEAR({x})", "HANDEMPTY"},
            {f"HOLDING({x})", f"CLEAR({y})"}
        )


def goal_stack_planning(initial, goals):
    state = set(initial)
    stack = [("GOAL", g) for g in reversed(goals)]
    plan = []

    while stack:
        kind, item = stack.pop()

        if kind == "ACTION":
            required = preconditions(item)

            if not all(p in state for p in required):
                print("Precondition failed:", item)
                return None

            add, delete = effects(item)
            state.difference_update(delete)
            state.update(add)
            plan.append(item)
            continue

        if item in state:
            continue

        if item.startswith("ON("):
            x, y = item[3:-1].split(",")
            action = ("STACK", x, y)
        elif item.startswith("HOLDING("):
            x = item[8:-1]
            action = ("PICKUP", x)
        else:
            print("Cannot achieve:", item)
            return None

        stack.append(("ACTION", action))

        for p in reversed(preconditions(action)):
            stack.append(("GOAL", p))

    if not all(g in state for g in goals):
        return None

    return plan, state


initial = initial_state()
goals = ["ON(x,y)", "ON(z,w)"]

print("Initial state:", sorted(initial))
print("Goal state:", goals)

result = goal_stack_planning(initial, goals)

if result:
    plan, final_state = result

    print("\nGoal Stack Plan:")
    for i, action in enumerate(plan, 1):
        print(i, action)

    print("\nFinal state:", sorted(final_state))
    print("Goal achieved:", all(g in final_state for g in goals))
