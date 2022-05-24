import sys
from collections import deque
sys.setrecursionlimit(100000)
def backtrack(board, q, prev_card, card_count, sex):
    i_move = [-1,1,0,0]
    j_move = [0,0,-1,1]
    if card_count == 0:
        print(sex)
        return
    while q:
        r, c, count = q.popleft()
        # 전에 뒤집은 카드와 같은경우 두번째 enter
        if board[r][c] == prev_card[0]:
            board[r][c] = 0
            board[prev_card[1][0]][prev_card[1][1]] = 0
            count += 1
            card_count -= 1
            prev_card[0] = -1
        # 현재 커서가 카드인데 처음 카드를 고른 경우 enter
        elif prev_card[0] == -1 and board[r][c] != 0:
            prev_card[0] = board[r][c]
            prev_card[1][0] = r
            prev_card[1][1] = c
            count += 1
        #그냥 상 하 좌 우
        for i in range(4):
            next_i = r + i_move[i]
            next_j = c + j_move[i]
            if 0 <= next_i < 4 and 0 <= next_j < 4:
                q.append((next_i, next_j , count + 1))
        #ctrl 상 하 좌 우
        #상
        for i in range(r-1,-1,-1):
            if board[i][c] != 0:
                q.append((i, c, count + 1))
                break
        #하
        for i in range(r+1,4):
            if board[i][c] != 0:
                q.append((i,c,count + 1))
                break
        #좌
        for j in range(c-1, -1 ,-1):
            if board[r][j] != 0:
                q.append((r,j,count + 1))
                break
        #우
        for j in range(c+1, 4):
            if board[r][j] != 0:
                q.append((r,j,count + 1))
                break
        backtrack(board, q, prev_card, card_count, count)


def solution(board, r, c):
    answer = []
    q = deque()
    q.append((r, c, 0))
    card = {1:0 , 2:0, 3:0, 4:0, 5:0, 6:0}
    prev_card = [-1, [-1, -1]]
    backtrack(board, q, prev_card, 3, 0)
    return answer
board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
solution(board, r, c)
