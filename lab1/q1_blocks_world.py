# Goal stack planning - blocks world
# Initial: A, B, C, D on the table
# Goal: ON(A,C) and ON(D,B)

state = {"HANDEMPTY"}
for b in "ABCD":
    state.add(f"ONTABLE({b})")
    state.add(f"CLEAR({b})")

goal = ["ON(A,C)", "ON(D,B)"]


def pickup(x):
    pre = [f"ONTABLE({x})", f"CLEAR({x})", "HANDEMPTY"]
    add = {f"HOLDING({x})"}
    rem = {f"ONTABLE({x})", f"CLEAR({x})", "HANDEMPTY"}
    return pre, add, rem


def stack(x, y):
    pre = [f"HOLDING({x})", f"CLEAR({y})"]
    add = {f"ON({x},{y})", f"CLEAR({x})", "HANDEMPTY"}
    rem = {f"HOLDING({x})", f"CLEAR({y})"}
    return pre, add, rem


def make_action(name):
    # name looks like "PICKUP(A)" or "STACK(A,C)"
    args = name[name.index("(") + 1:-1].split(",")
    return pickup(*args) if name.startswith("PICKUP") else stack(*args)


def achiever(pred):
    if pred.startswith("ON("):
        x, y = pred[3:-1].split(",")
        return f"STACK({x},{y})"
    if pred.startswith("HOLDING("):
        return f"PICKUP({pred[8:-1]})"
    return None


goal_stack = list(reversed(goal))
plan = []
step = 0

print("Initial state:", sorted(state))
print("Goal:", " & ".join(goal), "\n")

while goal_stack:
    step += 1
    print(f"Step {step}: stack (top first) = {goal_stack[::-1]}")
    top = goal_stack.pop()

    if top.startswith(("PICKUP", "STACK")):
        pre, add, rem = make_action(top)
        if not all(p in state for p in pre):
            print("  preconditions not met for", top)
            break
        state -= rem
        state |= add
        plan.append(top)
        print("  apply", top)
    elif top in state:
        print("  already true:", top)
    else:
        act = achiever(top)
        if act is None:
            print("  cannot achieve", top)
            break
        pre, _, _ = make_action(act)
        goal_stack.append(act)
        goal_stack.extend(reversed(pre))
        print(f"  {top} not true, push {act} and its preconditions")

print("\nPlan:")
for i, a in enumerate(plan, 1):
    print(f"{i}. {a}")
print("\nFinal state:", sorted(state))
print("Goal reached:", all(g in state for g in goal))
