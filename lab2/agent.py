def simple_agent(grid,start,dirty):
    q = []
    q.append(start)
    vis = [[False]*cols for _ in range (rows)]
    revisit = 0
    movement = 0
    op = 0
    it = 100
    while len(q) > 0 and dirty > 0 and it > 0:
        curr = q.pop(0)
        x = curr[0]
        y = curr[1]

        if vis[x][y]:
            revisit+=1
        else:
            vis[x][y] = True

        if grid[x][y] == "D":
            grid[x][y] = "C"
            op+=1
            dirty-=1

        if x-1 >=0 and grid[x-1][y]!="X":
            q.append((x-1,y))
            movement+=1

        if x+1 < rows and grid[x+1][y]!="X":
            q.append((x+1,y))
            movement+=1

        if y-1 >=0 and grid[x][y-1]!="X":
            q.append((x,y-1))
            movement+=1

        if y+1 < cols and grid[x][y+1]!="X":
            q.append((x,y+1))
            movement+=1

        it-=1
    print("--Simple Agent--")
    print("Dirty cell cleaned : ",op)
    print("Movements : ",movement)
    print("Total Actions : ",op + movement)
    print("Repeated Revisits : ",revisit)


def memory_agent(grid,start,dirty):
    q = []
    q.append(start)
    vis = [[False]*cols for _ in range (rows)]
    revisit = 0
    movement = 0
    op = 0
    vis[start[0]][start[1]] = True
    while len(q) > 0 and dirty > 0:
        curr = q.pop(0)
        x = curr[0]
        y = curr[1]

        if grid[x][y] == "D":
            grid[x][y] = "C"
            op+=1
            dirty-=1

        if x-1 >=0 and grid[x-1][y]!="X" and not vis[x-1][y]:
            q.append((x-1,y))
            vis[x-1][y] = True
            movement+=1

        if x+1 < rows and grid[x+1][y]!="X" and not vis[x+1][y]:
            q.append((x+1,y))
            vis[x+1][y] = True
            movement+=1

        if y-1 >=0 and grid[x][y-1]!="X" and not vis[x][y-1]:
            q.append((x,y-1))
            vis[x][y-1] = True
            movement+=1

        if y+1 < cols and grid[x][y+1]!="X" and not vis[x][y+1]:
            q.append((x,y+1))
            vis[x][y+1] = True
            movement+=1


    print("--Memory Agent--")
    print("Dirty cell cleaned : ",dirty)
    print("Movements : ",movement)
    print("Total Actions : ",op + movement)
    print("Repeated Revisits : ",revisit)

rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of coloumns : "))

grid = []
start = []
dirty = 0
for i in range(rows):
    row = input().split()
    grid.append(row)
        
for i in range(rows):
    for j in range(cols) :
        if grid[i][j] == "S":
            start = (i,j)
        elif grid[i][j] == "D":
            dirty+=1


simple_agent(grid,start,dirty)
print("\n")
memory_agent(grid,start,dirty)
