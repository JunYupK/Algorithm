from collections import Counter
s = list(input())
answer = ''
center = ''
s.sort()
counter = Counter(s)
for k,v in counter.items():
    if v % 2 != 0:
        center += k

if len(center) > 1:
    print("I'm Sorry Hansoo")
    exit(0)
if len(s) % 2 == 0 and len(center) >= 1 or len(s) %2 != 0 and len(center) == 0:
    print("I'm Sorry Hansoo")
    exit(0)
counter = sorted(counter.items())
#홀수
for k, v in counter:
    for _ in range(v//2):
        answer += k
tmp = answer[::-1]
if len(center) == 1:
    answer += center
print(answer+tmp)