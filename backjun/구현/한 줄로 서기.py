from itertools import permutations
N = int(input())
a = list(map(int, input().split()))
answer = []
for human in permutations([i for i in range(1,N+1)], N):
    count = 0
    for i in range(N):
        up_count = 0
        for j in range(N):
            if i+1 == human[j]:
                break
            if i+1 < human[j]:
                up_count += 1
        if up_count == a[i]:
            count += 1
        else:
            break
    if count == N:
        answer = human
print(*answer)