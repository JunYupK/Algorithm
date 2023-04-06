N = int(input())
board = []
answer = 0
for _ in range(N):
    board.append(list(input()))
def check_count():
    global answer
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                count += 1
                answer = max(count, answer)
            else:
                count = 1
        count = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                count += 1
                answer = max(count, answer)
            else:
                count = 1

for i in range(N):
    for j in range(1,N):
        if board[i][j] != board[i][j-1]:
            board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
            check_count()
            board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
        if board[j][i] != board[j-1][i]:
            board[j][i], board[j-1][i] = board[j-1][i], board[j][i]
            check_count()
            board[j][i], board[j-1][i] = board[j-1][i], board[j][i]

print(answer)
