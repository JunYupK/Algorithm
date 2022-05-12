def solution(m, n, board):
    answer = 0
    new_board = []
    for i in board:
        new_board.append(list(i))
    while 1:
        count = 0
        tmp = [[False] * n for _ in range(m)]
        for i in range(m):
            if i == len(board) - 1:
                continue
            for j in range(n):
                if j == len(board[i]) -  1:
                    continue
                if new_board[i][j] == '':
                    continue
                if new_board[i][j] == new_board[i+1][j] and new_board[i][j] == new_board[i+1][j+1] and new_board[i][j] == new_board[i][j+1]:
                    count += 1
                    tmp[i][j] = True
                    tmp[i][j+1] = True
                    tmp[i+1][j] = True
                    tmp[i+1][j+1] = True
        if count == 0:
            break
        #check 된곳 삭제
        for i in range(m):
            for j in range(n):
                if tmp[i][j] == True:
                    new_board[i][j] = ''
        for i in range(m-2, -1, -1):
            for j in range(n):
                ti = i
                if new_board[i][j] == '':
                    continue
                while 1:
                    if ti == m - 1:
                        break
                    if new_board[ti+1][j] != '':
                        break
                    new_board[ti+1][j] = new_board[ti][j]
                    new_board[ti][j] = ''
                    ti += 1

    for i in range(m):
        for j in range(n):
            if new_board[i][j] == '':
                answer += 1
    return answer

board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
tmp = []
m = 6
n = 6
solution(m,n,board)

#빡구현 문제다. 괜히 n의 수가 적은데 괜히 효율적인 코드를 짜보려다가 시간을 꽤나 썼다. n의 수가 적으면 그대로 구현하는 연습도 해야할것같다.