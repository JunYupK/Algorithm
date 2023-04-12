import sys
input = sys.stdin.readline
N = int(input())
time = []
answer = []
checkSum = [0] * 1442
checkSum[1440] = 1
for _ in range(N):
    a, b = map(int,input().split())
    a_tmp = []
    b_tmp = []
    while a != 0:
        a_tmp.append(a%10)
        b_tmp.append(b%10)
        a = a//10
        b = b // 10
    a_mit= a_tmp[1] * 10 + a_tmp[0]
    a_hour = a_tmp[3] * 10 + a_tmp[2]
    b_mit= b_tmp[1] * 10 + b_tmp[0]
    b_hour = b_tmp[3] * 10 + b_tmp[2]
    time.append((a_hour * 60 + a_mit, b_hour * 60 + b_mit))
time.sort()
for start, end in time:
    start -= 10
    end += 10
    checkSum[start] += 1
    checkSum[end+1] -= 1

for i in range(1, len(checkSum)):
    checkSum[i] = checkSum[i-1] + checkSum[i]
start, end = 600, 601
flag = False
while end <= 1440:
    print(start, end)
    if checkSum[end] == 0:
        end += 1
    else:
        if checkSum[start] == 0:
            answer.append(end - start)
            start = end
            end += 1
            continue
        else:
            start += 1
            end += 1
print(answer)
if len(answer) == 0:
    print(0)
else:
    print(max(answer))
