
n, m = map(int,input().split())
s_set = set()
for _ in range(n):
    s_set.add(str(input()))
count = 0
for _ in range(m):
    s = str(input())
    if s in s_set:
        count += 1

print(count)