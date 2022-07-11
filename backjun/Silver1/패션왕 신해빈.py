import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = []
    for _ in range(n):
        tmp = sys.stdin.readline().split()
        clothes.append(tmp)
    answer = 1
    types = [y for x, y in clothes]
    counts = [types.count(type) for type in set(types)]
    for c in counts:
        answer *= c + 1
    print(answer-1)