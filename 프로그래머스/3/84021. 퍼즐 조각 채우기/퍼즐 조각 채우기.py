from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(board, visited, flag, x, y):
    visited[x][y] = True
    q = deque()
    q.append((x,y))
    n = len(board)
    puzzle = []
    while q:
        x, y = q.popleft()
        puzzle.append([x,y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            
            if visited[nx][ny] is False and board[nx][ny] == flag:
                q.append((nx,ny))
                visited[nx][ny] = True
    return puzzle

def puzzleToArr(puzzle):
    min_x = min(puzzle, key=lambda x:x[0])[0]
    max_x = max(puzzle, key=lambda x:x[0])[0]
    min_y = min(puzzle, key=lambda x:x[1])[1]
    max_y = max(puzzle, key=lambda x:x[1])[1]
    row = max_x - min_x + 1
    col = max_y - min_y + 1
    arr = [[0] * col for _ in range(row)]
    for x, y in puzzle:
        arr[x][y] = 1
    # print(arr)
    return arr
    
def rotate90(arr):
    n = len(arr)
    m = len(arr[0])
    if n == 1 and m == 1:
        return arr
    tmp = [[0] * n for _ in range(m)]
    ni = 0
    nj = n-1
    for i in range(n):
        ni = 0
        for j in range(m):
            tmp[ni][nj] = arr[i][j]
            ni += 1
        nj -= 1
    return tmp
def compare(left, right):
    lx = len(left)
    ly = len(left[0])
    rx = len(right)
    ry = len(right[0])
    if lx != rx or ly != ry:
        return False
    
    for i in range(lx):
        for j in range(ly):
            if(left[i][j] != right[i][j]):
                return False
    return True
def count_puzzle(puzzle):
    count = 0
    for i in puzzle:
        for j in i:
            if j == 1:
                count += 1
    return count
def solution(game_board, table):
    answer = 0
    n = len(game_board)
    game_puzzle = []
    table_puzzle = []
    game_arr = []
    table_arr = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False and game_board[i][j] == 0:
                tmp = bfs(game_board,visited,0,i,j)
                min_x = min(tmp, key=lambda x:x[0])[0]
                min_y = min(tmp, key=lambda x:x[1])[1]
                for k in range(len(tmp)):
                    tmp[k][0] -= min_x
                    tmp[k][1] -= min_y
                game_puzzle.append(tmp)
    
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] is False and table[i][j] == 1:
                tmp = bfs(table,visited,1,i,j)
                min_x = min(tmp, key=lambda x:x[0])[0]
                min_y = min(tmp, key=lambda x:x[1])[1]
                for k in range(len(tmp)):
                    tmp[k][0] -= min_x
                    tmp[k][1] -= min_y
                table_puzzle.append(tmp)

    for puzzle in game_puzzle:
        game_arr.append(puzzleToArr(puzzle))
    for puzzle in table_puzzle:
        table_arr.append(puzzleToArr(puzzle))
    
    check = set()
    #비교
    for i in range(len(game_arr)):
        for j in range(len(table_arr)):
            if j in check:
                continue
            next_flag = False
            tmp = table_arr[j]
            for _ in range(4):
                tmp = rotate90(tmp)
                flag = compare(game_arr[i], tmp)
                if flag is True:
                    check.add(j)
                    next_flag = True
                    answer += count_puzzle(tmp)
                    break
            if next_flag is True:
                break
    print(check)
    print(answer)
    return answer