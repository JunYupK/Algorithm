N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int,input().split())))
for i in range(1, N):
    print(data[i][0], data[i][1], data[i][2])
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    data[i][1] = min(data[i - 1][0], data[i - 1][2]) + data[i][1]
    data[i][2] = min(data[i - 1][0], data[i - 1][1]) + data[i][2]
    print(data[i][0], data[i][1], data[i][2])

print(min(data[N-1][0],data[N-1][1], data[N-1][2]))