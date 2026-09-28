from collections import deque
import heapq


def findPoints(matrix):
    start = pickup = goal = None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                start = (i, j)
            elif matrix[i][j] == 'P':
                pickup = (i, j)
            elif matrix[i][j] == 'G':
                goal = (i, j)

    return start, pickup, goal


def bfs(matrix, start, goal):
    n = len(matrix)
    m = len(matrix[0])

    q = deque()
    q.append(start)

    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    parent = {start: None}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()

        if (x, y) == goal:
            break

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if matrix[nx][ny] == 'X':
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            parent[(nx, ny)] = (x, y)
            q.append((nx, ny))

    if goal not in parent:
        return []

    path = []
    curr = goal

    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return path


def goalBasedAgent(matrix):
    start, pickup, goal = findPoints(matrix)

    path1 = bfs(matrix, start, pickup)
    path2 = bfs(matrix, pickup, goal)

    moves1 = len(path1) - 1
    moves2 = len(path2) - 1

    return {
        "StartToPickup": path1,
        "PickupToGoal": path2,
        "Stage1Movements": moves1,
        "Stage2Movements": moves2,
        "TotalMovements": moves1 + moves2
    }


def calculateCost(cost):
    distance, energy, risk, traffic = cost

    return (
        0.4 * distance +
        0.3 * energy +
        0.2 * risk +
        0.1 * traffic
    )


def minimumCostPath(matrix, start, goal, cellCosts):
    n = len(matrix)
    m = len(matrix[0])

    pq = []
    heapq.heappush(pq, (0, start))

    distance = {start: 0}
    parent = {start: None}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        cost, current = heapq.heappop(pq)

        if current == goal:
            break

        if cost > distance[current]:
            continue

        x, y = current

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if matrix[nx][ny] == 'X':
                continue

            nextCell = (nx, ny)

            # default:
            # distance = 1
            # energy = 1
            # risk = 0
            # traffic = 0
            travelInfo = cellCosts.get(
                nextCell,
                (1, 1, 0, 0)
            )

            moveCost = calculateCost(travelInfo)
            newCost = cost + moveCost

            if nextCell not in distance or newCost < distance[nextCell]:
                distance[nextCell] = newCost
                parent[nextCell] = current

                heapq.heappush(
                    pq,
                    (newCost, nextCell)
                )

    if goal not in parent:
        return [], 0

    path = []
    curr = goal

    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()

    return path, distance[goal]


def utilityBasedAgent(matrix, cellCosts):
    start, pickup, goal = findPoints(matrix)

    path1, cost1 = minimumCostPath(
        matrix,
        start,
        pickup,
        cellCosts
    )

    path2, cost2 = minimumCostPath(
        matrix,
        pickup,
        goal,
        cellCosts
    )

    moves1 = len(path1) - 1
    moves2 = len(path2) - 1

    return {
        "StartToPickup": path1,
        "PickupToGoal": path2,
        "Stage1Movements": moves1,
        "Stage2Movements": moves2,
        "TotalMovements": moves1 + moves2,
        "Stage1Cost": round(cost1, 2),
        "Stage2Cost": round(cost2, 2),
        "TotalCost": round(cost1 + cost2, 2)
    }


def main():

    matrix = [
        ['S','R','R','X','R','R','R','R','R','R'],
        ['X','X','R','R','R','X','R','X','R','R'],
        ['R','R','R','X','R','R','R','P','R','R'],
        ['R','X','R','R','R','X','R','R','R','X'],
        ['R','R','R','X','R','R','X','R','R','R'],
        ['X','R','R','R','R','R','R','R','X','R'],
        ['R','R','X','R','X','R','R','R','R','R'],
        ['R','R','R','R','R','X','R','X','R','R'],
        ['R','X','R','R','R','R','R','R','R','R'],
        ['R','R','R','X','R','R','R','R','X','G']
    ]

   
    cellCosts = {
        (1,3): (1,1,10,10),
        (1,4): (1,1,10,10),
        (2,4): (1,1,10,10),
        (2,5): (1,1,10,10),
        (2,6): (1,1,10,10),

        (3,7): (1,1,10,10),
        (4,7): (1,1,10,10),
        (5,7): (1,1,10,10),
        (6,7): (1,1,10,10)
    }

    goalResult = goalBasedAgent(matrix)

    print("\n--- Goal Based Agent ---")

    print("S -> P Route:")
    print(goalResult["StartToPickup"])

    print("S -> P Movements:",
          goalResult["Stage1Movements"])

    print("\nP -> G Route:")
    print(goalResult["PickupToGoal"])

    print("P -> G Movements:",
          goalResult["Stage2Movements"])

    print("Total Movements:",
          goalResult["TotalMovements"])


    utilityResult = utilityBasedAgent(
        matrix,
        cellCosts
    )

    print("\n--- Utility Based Agent ---")

    print("S -> P Route:")
    print(utilityResult["StartToPickup"])

    print("S -> P Movements:",
          utilityResult["Stage1Movements"])

    print("S -> P Cost:",
          utilityResult["Stage1Cost"])

    print("\nP -> G Route:")
    print(utilityResult["PickupToGoal"])

    print("P -> G Movements:",
          utilityResult["Stage2Movements"])

    print("P -> G Cost:",
          utilityResult["Stage2Cost"])

    print("Total Movements:",
          utilityResult["TotalMovements"])

    print("Total Cost:",
          utilityResult["TotalCost"])


if __name__ == "__main__":
    main()