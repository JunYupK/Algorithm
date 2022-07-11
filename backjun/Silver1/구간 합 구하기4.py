import sys
n, m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
sum_data = []
sum_data.append(data[0])
for i in range(1,len(data)):
    sum_data.append(data[i]  + sum_data[i-1])
for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    i -= 1
    j -= 1
    if i == 0:
        print(sum_data[j])
        continue
    print(sum_data[j] - sum_data[i-1])