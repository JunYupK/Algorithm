from itertools import combinations
# from extratypes import Point2D
def solution(A):
    # write your code in Python 3.6
    answer = 0
    for c in combinations(A, 3):
        x1, y1 = c[0]
        x2, y2 = c[1]
        x3, y3 = c[2]
        a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        if a == 0:
            answer += 1
    if answer == 0:
        answer = -1
    return answer

A = [(0,0), (1,1), (2,2), (3,2), (3,3), (4,2), (5,1)]
solution(A)
