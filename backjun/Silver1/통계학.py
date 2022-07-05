import sys
from collections import Counter
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()
print(round(sum(data)/n))
if n % 2 == 0:
    i = n//2
    print((data[i]+data[i-1])//2)
else:
    i = n//2
    print(data[i])
counter = dict(Counter(data))
counter = sorted(counter.items(), key=lambda x:x[1],reverse=True)
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])
if n > 1:
    print(abs(data[-1] - data[0]))
else:
    print(0)