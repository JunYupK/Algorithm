from collections import deque
n, m = map(int, input().split())
board = [[-1]*10 for _ in range(10)]
for _ in range(n):
    x, y = map(int,input().split())
    board[(x//10)][(x%10) - 1] = y
for _ in range(m):
    x, y = map(int,input().split())
    board[(x//10)][(x%10) - 1] = y
visited = [[False] * 10 for _ in range(10)]
q = deque()
q.append((0,0,0))
visited[0][0] = True
while q:
    x, y, count = q.popleft()
    move = (x*10) + y +1
    if move == 100:
        print(count)
        break
    for i in range(1,7):
        next_move = move + i
        if next_move == 100:
            q.append((9,9,count+1))
            break
        next_x = next_move // 10
        next_y = next_move % 10 -1
        if next_x > 9 or next_y > 9:
            continue
        if visited[next_x][next_y] is False and board[next_x][next_y] != -1:
            tmp = board[next_x][next_y]
            q.append((tmp//10, tmp%10-1,count+1))
            visited[next_x][next_y] = True
            visited[tmp//10][tmp%10-1] = True
        elif visited[next_x][next_y] is False and board[next_x][next_y] == -1:
            q.append((next_x, next_y,count+1))
            visited[next_x][next_y] = True