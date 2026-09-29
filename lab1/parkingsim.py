rows = int(input("enter the number of rows : "))
cols = int(input("enter the number of cols : "))

grid = []
entrance = None
print("enter parking grid")
for i in rows:
    for j in cols:
        grid[i][j] = input()
        if grid[i][j] == "E":
            entrance = (i,j)
            

if entrance is None:
    print("Parking lot has no entrance")
    exit()
    

q = []
q.append(entrance)

vis = []
vis.append(entrance)

parent = {}

while q:
    curr = q.pop(0)
    x = curr[0]
    y = curr[1]
    
    if grid[x][y]=="A":
        target = curr
        break
    
    if x - 1 >= 0:
        if (x - 1, y) not in vis:
            if grid[x - 1][y] == "R" or grid[x - 1][y] == "A":
                vis.append((x - 1, y))
                parent[(x - 1, y)] = curr
                q.append((x - 1, y))

    if x + 1 < rows:
        if (x + 1, y) not in vis:
            if grid[x + 1][y] == "R" or grid[x + 1][y] == "A":
                vis.append((x + 1, y))
                parent[(x + 1, y)] = curr
                q.append((x + 1, y))

    if y - 1 >= 0:
        if (x, y - 1) not in vis:
            if grid[x][y - 1] == "R" or grid[x][y - 1] == "A":
                vis.append((x, y - 1))
                parent[(x, y - 1)] = curr
                q.append((x, y - 1))

    if y + 1 < cols:
        if (x, y + 1) not in vis:
            if grid[x][y + 1] == "R" or grid[x][y + 1] == "A":
                vis.append((x, y + 1))
                parent[(x, y + 1)] = curr
                q.append((x, y + 1))


if target is None:
    print("No parking available")
    exit()
    

path = []

while target !=entrance:
    path.append(target)
    target = parent[target]
    
path.append(entrance)
path.reverse()

print(f"nearest spot = {path[-1]}")

for p in path:
    print(p)
    



# Example test input (the current draft also has initialization errors):
# 3
# 4
# E R X R
# X R X A
# R R R R






