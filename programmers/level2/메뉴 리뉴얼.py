from itertools import permutations, combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for count in course:
        tmp = []
        for order in orders:
            com = combinations(sorted(order), count)
            tmp += com
        counter = Counter(tmp)
        print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2]
print(solution(orders, course))