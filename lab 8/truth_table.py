
from itertools import product

def truth_input(name):
    while True:
        value = input(f"{name} (T/F): ").strip().upper()
        if value in ("T", "TRUE"):
            return True
        if value in ("F", "FALSE"):
            return False
        print("Enter T or F.")

p = truth_input("p: x is a student")
q = truth_input("q: x has an ID number")
r = truth_input("r: x gets good skills")
s = truth_input("s: x has a good package")

print("\nResults for entered values:")
print("p AND q =", p and q)
print("p AND r AND s =", p and r and s)
print("(p AND r) -> s =", not (p and r) or s)
print("s <-> r =", s == r)

def truth_table(name, variables, expression):
    print("\n", name)
    print(" ".join(variables), "| Result")
    print("-" * 25)

    for values in product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))
        result = expression(env)
        row = " ".join("T" if v else "F" for v in values)
        print(row, "|", "T" if result else "F")

truth_table(
    "p AND q", ["p", "q"],
    lambda e: e["p"] and e["q"]
)

truth_table(
    "p AND r AND s", ["p", "r", "s"],
    lambda e: e["p"] and e["r"] and e["s"]
)

truth_table(
    "(p AND r) -> s", ["p", "r", "s"],
    lambda e: not (e["p"] and e["r"]) or e["s"]
)

truth_table(
    "s <-> r", ["s", "r"],
    lambda e: e["s"] == e["r"]
)
