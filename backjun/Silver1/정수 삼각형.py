n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

for i in range(1, n):
    for k in range(len(data[i])):
        if k == 0:
            data[i][k] = data[i-1][k] + data[i][k]
        elif k == len(data[i]) - 1:
            data[i][k] = data[i-1][k-1] + data[i][k]
        else:
            data[i][k] = max(data[i-1][k-1], data[i-1][k]) + data[i][k]
print(max(data[-1]))