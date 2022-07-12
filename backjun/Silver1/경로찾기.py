#취코테 책의 벨만포드 알고리즘 참고하여 다시 풀어보기
from collections import deque
n = int(input())
board = []
for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
visited = [[0]* n for _ in range(n)]
q = deque()
def bfs(x):
    chk = [0] * n
    while q:
        nx = q.popleft()
        for i in range(n):
            if chk[i] == 0 and board[nx][i] == 1:
                q.append(i)
                chk[i] = 1
                visited[x][i] = 1
for i in range(n):
    q.append(i)
    bfs(i)
for v in visited:
    print(*v)
