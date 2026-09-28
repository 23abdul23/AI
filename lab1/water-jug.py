jug4 = 0
jug3 = 0

print(f"Initial State: 4L={jug4}, 3L={jug3}")

jug3 = 3
print(f"Fill 3L jug       : 4L={jug4}, 3L={jug3}")

jug4 = 3
jug3 = 0
print(f"Pour into 4L jug  : 4L={jug4}, 3L={jug3}")

jug3 = 3
print(f"Fill 3L jug again : 4L={jug4}, 3L={jug3}")

jug3 = 2
jug4 = 4
print(f"Fill 4L completely: 4L={jug4}, 3L={jug3}")

jug4 = 0
print(f"Empty 4L jug      : 4L={jug4}, 3L={jug3}")

jug4 = 2
jug3 = 0
print(f"Transfer remaining: 4L={jug4}, 3L={jug3}")

print("\nGoal achieved: 4L jug contains exactly 2 liters.")