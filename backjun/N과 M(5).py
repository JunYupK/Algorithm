from itertools import combinations,permutations
global n, m
def backtracking(num,data,check,k):
    if len(num) == m:
        for i in num:
            print(i, end=" ")
        print()



n , m = map(int,input().split())
data = (list(map(int,input().split())))
check = [False] * n
num = []
for com in permutations(data, m):
    num.append(com)

num = sorted(num)
for x in num:
    for y in x:
        print(y, end= " ")
    print()