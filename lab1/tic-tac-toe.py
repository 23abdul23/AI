board = []

print("Enter the Tic-Tac-Toe board (3 rows):")
for _ in range(3):
    row = input().split()
    board.append(row)

winner = None

for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
        winner = board[i][0]

for j in range(3):
    if board[0][j] == board[1][j] == board[2][j] and board[0][j] != "_":
        winner = board[0][j]

if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
    winner = board[0][0]

if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
    winner = board[0][2]

if winner:
    print(f"{winner} Wins!")
else:
    print("Draw")