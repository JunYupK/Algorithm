import sys
input = sys.stdin.readline
R, C, M = map(int,input().split())
board = [[(0,0,0)] * (C+1) for _ in range(R+1)]
# for i in range(C+1):
#     board[0][i] = 1
# for i in range(R+1):
#     board[i][0] = 1
for _ in range(M):
    r, c, s, d, z = map(int,input().split())
    board[r][c] = (s,d,z)
def move_shark():
    for i in range(1, R+1):
        for j in range(1, C+1):
            if board[i][j] != (0,0,0):
                speed, dir, size = board[i][j]
                if dir == 1:
                    check = i - 1
                    if speed >= check:
                        dir = 2
                        check = speed - check

                elif dir == 2:
                    check = i + speed
                    if check > R:
                        check = R - (check % R)
                        dir = 1
                    print(check, j)
                    board[check][j] = (speed, dir, size)
                elif dir == 3:
                    check = j - 1
                    if speed >= check:
                        dir = 4
                        check = speed - check
                    board[i][j + check] = (speed, dir, size)
                elif dir == 4:
                    check = j + speed
                    if check > C:
                        check = C - (check % C)
                        dir = 3
                    board[i][check] = (speed, dir, size)
                # board[i][j] = (0,0,0)
for i in range(R+1):
    print(board[i])
print()
move_shark()

for i in range(R+1):
    print(board[i])


