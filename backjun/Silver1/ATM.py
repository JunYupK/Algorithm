import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
human = []
for i in range(1,n+1):
    human.append((i,data[i-1]))
human.sort(key=lambda x:x[1])
time = 0
answer = 0
for h,t in human:
    time += t
    answer += time
print(answer)