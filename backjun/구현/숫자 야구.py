import sys
from collections import Counter
from itertools import permutations
input = sys.stdin.readline
qus = []
numbers = []
answer = {}
items = [1,2,3,4,5,6,7,8,9]
numbers = list(permutations(items, 3))
N = int(input())
for _ in range(N):
    n, st, ball = map(int,input().split())
    n = list(str(n))
    qus.append([[int(n[0]), int(n[1]), int(n[2])],st,ball])

for num in numbers:
    x = num[0] * 100 + num[1] * 10 + num[2]
    answer[x] = 1
for n, st, ball in qus:
    counter = Counter(n)
    for num in numbers:
        tmp_s, tmp_b = 0, 0
        if num[0] == n[0]:
            tmp_s += 1
        if num[1] == n[1]:
            tmp_s += 1
        if num[2] == n[2]:
            tmp_s += 1
        if num[0] in counter:
            tmp_b += 1
        if num[1] in counter:
            tmp_b += 1
        if num[2] in counter:
            tmp_b += 1
        tmp_b -= tmp_s
        if tmp_s == st and tmp_b == ball:
            continue
        else:
            x = num[0] * 100 + num[1] * 10 + num[2]
            answer[x] = 0
count = 0
for k, v in answer.items():
    if v == 1:
        count += 1

print(count)
