from itertools import combinations,permutations
def solution(ability):
    answer = 0
    N = len(ability)
    M = len(ability[0])
    students = [i for i in range(N)]
    sports = [i for i in range(M)]
    for c in permutations(students, M):
        _sum = 0
        for i in range(len(c)):
            _sum += ability[c[i]][i]
        if _sum > answer:
            answer = _sum
    return answer
solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])