import math

board = [" "] * 9

def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()


def winner(b):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, c, d in wins:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]

    if " " not in b:
        return "draw"

    return None


def minimax(b, maximizing):
    result = winner(b)

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "draw":
        return 0

    if maximizing:
        best = -math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)

        return best


def best_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


print("You are X")
print("AI is O")
print("Positions:")
print(" 0 | 1 | 2 ")
print("---+---+---")
print(" 3 | 4 | 5 ")
print("---+---+---")
print(" 6 | 7 | 8 ")

while True:
    print_board()
    move = int(input("Your move (0-8): "))

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"

    result = winner(board)

    if result:
        print_board()
        if result == "X":
            print("You win!")
        elif result == "O":
            print("AI wins!")
        else:
            print("Draw!")
        break

    ai_move = best_move()
    board[ai_move] = "O"

    print(f"AI chooses: {ai_move}")

    result = winner(board)

    if result:
        print_board()
        if result == "X":
            print("You win!")
        elif result == "O":
            print("AI wins!")
        else:
            print("Draw!")
        break