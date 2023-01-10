import sys
input = sys.stdin.readline
R, C, T = map(int,input().split())
board = []
clean = []
moves = [(-1,0),(1,0),(0,1),(0,-1)]
for i in range(R):
    tmp = list(map(int,input().split()))
    if tmp[0] == -1:
        clean.append((i,0))
    board.append(tmp)

def diffusion(i, j, cost):
    count = 0
    diffuse = []
    for move in moves:
        next_i, next_j = move[0] + i , move[1] + j
        if 0 <= next_i < R and 0 <= next_j < C and board[next_i][next_j] != -1:
            count += 1
            diffuse.append((next_i,next_j))
    if count == 0:
        return
    for dif in diffuse:
        board[dif[0]][dif[1]] += cost // 5
    board[i][j] -= ((cost // 5) * count)
def rotate_up(x):
    for i in range(x-2, -1, -1):
        board[i + 1][0] = board[i][0]
    for j in range(1,C):
        board[0][j-1]= board[0][j]
    for i in range(1, x+1):
        board[i-1][C-1] = board[i][C-1]
    for j in range(C-2, 0, -1):
        board[x][j+1] = board[x][j]
    board[x][1] = 0
def rotate_down(x):
    for i in range(x+2, R):
        board[i-1][0] = board[i][0]
    for j in range(1, C):
        board[R-1][j-1] = board[R-1][j]
    for i in range(R-2, x-1, -1):
        board[i+1][C-1] = board[i][C-1]
    for j in range(C-2, 0, -1):
        board[x][j+1] = board[x][j]
    board[x][1] = 0
for _ in range(T):
    result = 0
    dust = []
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                dust.append((i,j, board[i][j]))

    for d in dust:
        diffusion(d[0],d[1],d[2])
    rotate_up(clean[0][0])
    rotate_down(clean[1][0])
    for i in range(R):
        result += sum(board[i])
print(result + 2)
