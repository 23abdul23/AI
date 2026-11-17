# Research fellowship knowledge base - forward chaining

print("(i) Policies in FOL")
print("1. forall x (Student(x) -> exists y (Course(y) & Studies(x,y)))")
print("2. forall x forall y (Student(x) & Course(y) & Studies(x,y) & Passed(x,y) -> Qualified(x))")
print("3. forall x forall p (Qualified(x) & Professor(p) & Supervises(p,x) -> Researcher(x))")
print("4. forall x (Researcher(x) -> Eligible(x))")

facts = {
    ("Student", "Ravi"), ("Student", "Anu"),
    ("Course", "AI"), ("Course", "ML"),
    ("Studies", "Ravi", "AI"), ("Passed", "Ravi", "AI"),
    ("Studies", "Anu", "ML"),
    ("Professor", "DrSharma"),
    ("Supervises", "DrSharma", "Ravi"),
}

students = [f[1] for f in facts if f[0] == "Student"]
courses = [f[1] for f in facts if f[0] == "Course"]
profs = [f[1] for f in facts if f[0] == "Professor"]


def rule_qualified(kb):
    out = set()
    for x in students:
        for c in courses:
            if ("Studies", x, c) in kb and ("Passed", x, c) in kb:
                out.add(("Qualified", x))
    return out


def rule_researcher(kb):
    out = set()
    for x in students:
        for p in profs:
            if ("Qualified", x) in kb and ("Supervises", p, x) in kb:
                out.add(("Researcher", x))
    return out


def rule_eligible(kb):
    return {("Eligible", f[1]) for f in kb if f[0] == "Researcher"}


rules = [
    ("Rule 2 (Qualified)", rule_qualified),
    ("Rule 3 (Researcher)", rule_researcher),
    ("Rule 4 (Eligible)", rule_eligible),
]

print("\n(ii) Meaning of: forall x (Student(x) -> exists y (Course(y) & Studies(x,y)))")
print("Each student studies some course, but the course can differ per student.")
for s in students:
    taken = [f[2] for f in facts if f[0] == "Studies" and f[1] == s]
    print(f"  {s} studies {taken}")
print("Ravi studies AI and Anu studies ML, yet the statement holds.")
print("So it does not mean everyone studies the same course.")
print("Studies(Anu, AI) is not in the KB, so we cannot conclude every student studies AI.")

print("\n(iii) Deriving Eligible(Ravi)")
kb = set(facts)
step = 1
changed = True
while changed:
    changed = False
    for name, rule in rules:
        new = rule(kb) - kb
        for fact in sorted(new):
            print(f"Step {step}: {name} -> {fact[0]}({', '.join(fact[1:])})")
            step += 1
        if new:
            kb |= new
            changed = True

for who in ["Ravi", "Anu"]:
    print(f"Eligible({who}) derivable:", ("Eligible", who) in kb)
print("Anu has not passed any course and has no supervisor, so she is not eligible.")
