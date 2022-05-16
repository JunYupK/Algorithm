global n, m
def back_tracking(num, check, k):
    if len(num) == m:
        for x in num:
            print(x, end=' ')
        print()
        return
    for i in range(n):
        if len(num) >= 1 and k > i+1:
            continue
        num.append(i+1)
        back_tracking(num, check, i + 1)
        num.pop()


n , m = map(int,input().split())
data = (list(map(int,input().split())))
check = [False] * n
num = []
print(data)
back_tracking(num, check, 0)