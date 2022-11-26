
n = int(input())
board= []
for _ in range(n):
    board.append(list(map(int,input().split())))

count_one = 0
count_zero = 0
count_minus = 0
def dfs(x,y,n):
    global count_zero,count_one,count_minus
    num_check = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y + n):
            if board[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k * n // 3, y + l*n//3, n//3)
                return
    if num_check == -1:
        count_minus += 1
    elif num_check == 0:
        count_zero += 1
    else:
        count_one += 1
dfs(0,0,n)
print(count_minus)
print(count_zero)
print(count_one)