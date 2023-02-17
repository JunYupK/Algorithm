from collections import deque
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    N, M = len(maps), len(maps[0])
    board = []
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(N):
        board.append(list(maps[i]))

    def bfs(i,j):
        result = 0
        q = deque()
        q.append((i,j))
        visited[i][j] = True
        while q:
            x, y = q.popleft()
            result += int(board[x][y])
            for dx, dy in moves:
                nx,ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny <M:
                    x = 0



    return answer

solution(["X591X","X1X5X","X231X", "1XXX1"])