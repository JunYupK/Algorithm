import sys
n, m = map(int,sys.stdin.readline().split())
data = {}
for _ in range(n):
    tmp = sys.stdin.readline().split()
    data[tmp[0]] = tmp[1]
for _ in range(m):
    tmp = sys.stdin.readline().split()
    print(data[tmp[0]])