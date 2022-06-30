import sys
input = sys.stdin.readline

A, B = map(int, input().split())
m = input()
before = list(map(int, input().split()))

total = 0
power = 0
for b in before[::-1]:
    total += (b * (A ** power))
    power += 1

after = []
while total:
    after.append(str(total % B))
    total //= B

sys.stdout.write(' '.join(after[::-1]))
