from itertools import product
n , m = map(int,input().split())
data = (list(map(int,input().split())))
data = sorted(data)
check = [False] * n
num = []
for com in product(data, repeat = m):
    num.append(com)

num = sorted(num)
for x in num:
    for y in x:
        print(y, end= " ")
    print()