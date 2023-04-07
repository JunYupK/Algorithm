import sys
input = sys.stdin.readline
def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    _max, _min = max(x,y), min(x,y)
    if x == y:
        print(1)
        continue
    print(facto(_max)//(facto(_max - _min) * facto(_min)))