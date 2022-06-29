import copy
from itertools import combinations
from collections import deque
def bfs(board, position):
    x, y = position
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((x,y))
    while q:
        x, y  = q.popleft()
        board[x][y] = 2
        for i in range(4):
            next_x , next_y = x+dx[i], y + dy[i]
            if next_x < 0 or next_x > len(board)-1 or next_y < 0 or next_y > len(board[0]) -1:
                continue
            if board[next_x][next_y] == 0:
                q.append((next_x,next_y))
n , m = map(int, input().split())
board = []
wall = []
virus = []
answer = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            wall.append((i,j))
        if tmp[j] == 2:
            virus.append([i,j])
    board.append(tmp)
for c in combinations(wall,3):
    count = 0
    tmp = copy.deepcopy(board)
    for i,j in c:
        tmp[i][j] = 1
    for p in virus:
        bfs(tmp,p)
    for t in tmp:
        count += t.count(0)
    answer  = max(answer, count)
print(answer)