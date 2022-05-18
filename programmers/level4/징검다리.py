from itertools import combinations
from bisect import bisect_left, bisect_right
def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    for com in combinations(rocks, n):
        tmp = rocks[:]
        for x in com:
            tmp.remove(x)
        print(tmp)

    print(rocks)
    return answer

rocks = [2, 14, 11, 21, 17]
distance = 25
n = 2
solution(distance,rocks, n)