import sys
n, answer = map(int,sys.stdin.readline().split())
result = 0
coin = []
for _ in range(n):
    tmp = int(sys.stdin.readline())
    coin.append(tmp)
coin.sort(reverse=True)
for c in coin:
    if answer == 0:
        break
    if c <= answer:
        result += answer//c
        answer = answer % c

print(result)