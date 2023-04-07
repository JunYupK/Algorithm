N = int(input())
target = int(input())
board = [[0] * N for _ in range(N)]
start = N * N
count = N
moves = [(1,0),(0,1),(-1,0),(0,-1)]
pos_x, pos_y = -1, 0
while start != 0:
    direct = 0
    for i in range(count):
        pos_x, pos_y = pos_x + moves[direct][0] , pos_y + moves[direct][1]
        board[pos_x][pos_y] = start
        start -= 1
    direct += 1
    count -= 1
    for i in range(count):
        pos_x, pos_y = pos_x + moves[direct][0] , pos_y + moves[direct][1]
        board[pos_x][pos_y] = start
        start -= 1
    direct += 1
    for i in range(count):
        pos_x, pos_y = pos_x + moves[direct][0] , pos_y + moves[direct][1]
        board[pos_x][pos_y] = start
        start -= 1
    direct += 1
    count -= 1
    for i in range(count):
        pos_x, pos_y = pos_x + moves[direct][0] , pos_y + moves[direct][1]
        board[pos_x][pos_y] = start
        start -= 1
    if start == 1:
        board[pos_x+1][pos_y] = 1
        break

for i in range(N):
    for j in range(N):
        if board[i][j] == target:
            pos_x = i
            pos_y = j
        print(board[i][j], end= " ")
    print()
print(*[pos_x+1, pos_y+1])