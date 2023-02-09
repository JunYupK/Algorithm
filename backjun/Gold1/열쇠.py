import sys
from collections import deque
def dfs(start, keys, board):
    moves = [[-1,0], [1,0], [0,-1], [0,1]]
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    answer = 0
    q = deque()
    for position in start:
        i, j = position[0], position[1]
        if board[i][j].isalpha() and board[i][j].islower():
            keys[board[i][j].upper()] = True
        q.append(position)
    while q:
        x, y = q.popleft()
        if board[x][y] == '$':
            answer += 1
        for dx,dy in moves:
            nx, ny = dx + x, dy + y
            if 0 <= nx < len(board)-1 and 0 <= ny < len(board[0])-1:
                if visited[nx][ny] is False:
                    #벽이 아니거나 문서일 경우
                    if board[nx][ny] == '.' or board[nx][ny] == '$':
                        q.append((nx,ny))
                        visited[nx][ny] = True
                    # key를 습득한 경우 key꾸러미에 넣기
                    elif board[nx][ny] not in keys and board[nx][ny].isalpha() and board[nx][ny].islower():
                        keys[board[nx][ny].upper()] = True
                        q.append((nx,ny))
                        visited[nx][ny] = True
                        board[nx][ny] = '.'
                    # key에 있는 문일 경우 접근 가능
                    elif board[nx][ny] in keys:
                        q.append((nx,ny))
                        visited[nx][ny] = True
                        board[nx][ny] = '.'
    return [answer, keys, board]
def make_start_position(board,keys):
    position = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                if board[i][j] in keys or board[i][j] == '.':
                    position.append((i,j))
                elif board[i][j].isalpha() and board[i][j].islower():
                    keys[board[i][j].upper()] = True

    return [position, keys]
N = int(input())
for _ in range(N):
    h, w = map(int,input().split())
    board, start_position = [], []
    for i in range(h):
        tmp = list(input())
        board.append(tmp)
    tmp_keys = list(input())
    keys = {}
    for char in tmp_keys:
        if char == '0':
            break
        if char.isalpha():
            keys[char.upper()] = True
    stack = [len(keys)]
    while 1:
        start_position, keys = make_start_position(board,keys)
        ans ,keys, board = dfs(start_position,keys, board)
        if stack[-1] == len(keys):
            break
        stack.append(len(keys))
    print(ans)



