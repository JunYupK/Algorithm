from itertools import combinations
n , m = map(int,input().split())
data = (list(map(int,input().split())))
data = sorted(data)
check = [False] * n
num = []
for com in combinations(data, m):
    num.append(com)

num = sorted(num)
for x in num:
    for y in x:
        print(y, end= " ")
    print()