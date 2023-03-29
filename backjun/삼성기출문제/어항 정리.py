import sys
input = input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int, input().split()))
board = [arr]

def isStacked(levitation, lines):
    if len(levitation) > len(lines):
        return False
    else:
        return True
def rotate(levitation):
    n, m = len(levitation), len(levitation[0])
    result = []
    for j in range(m-1,-1,-1):
        tmp = []
        for i in range(n):
            tmp.append(levitation[i][j])
        result.append(tmp)
    return result
def stack(levitation, board):
    n = len(levitation)
    for i in range(n-1,-1,-1):
        board.insert(0, levitation[i])
    return board
def makeLevitation(board):
    result = []
    lines = []
    n = len(board)
    if n > 1:
        m = len(board[0])
    else:
        m = 0
    for i in range(n-1):
        result.append(board[i])
    tmp = []
    for i in range(m):
        tmp.append(board[n-1][i])
    result.append(tmp)
    for i in range(m,len(board[n-1])):
        lines.append(board[n-1][i])
    return result,lines

board.insert(0,[9])
print(board)
levi, line = makeLevitation(board)
print(levi)
print(line)
levi = rotate(levi)
print(stack(levi,line))