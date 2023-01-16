import sys
input = sys.stdin.readline
R, C = map(int ,input().split())
board = []
moves = [(-1,0),(1,0),(0,-1),(0,1)]
check = [False] * 26
global _max
_max = 0
for _ in range(R):
    tmp = list(input())
    tmp.pop()
    board.append(tmp)
def dfs(x,y, count):
    global _max
    for move in moves:
        next_x, next_y = x + move[0], y+move[1]
        if 0 <= next_x < R and 0 <= next_y < C and check[ord(board[next_x][next_y]) % 65] is False:
            check[ord(board[next_x][next_y]) % 65] = True
            dfs(next_x,next_y, count + 1)
            check[ord(board[next_x][next_y]) % 65] = False
    if _max < count:
        _max = count
check[ord(board[0][0])%65] = True
dfs(0,0,1)
print(_max)