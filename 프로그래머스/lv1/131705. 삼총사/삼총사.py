from itertools import combinations
def solution(number):
    answer = 0
    for c in combinations(number, 3):
        if sum(c) == 0:
            answer += 1
    return answer