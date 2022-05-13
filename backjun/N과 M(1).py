global n, m
def back_tracking(num, check, k):
    if len(num) == m:
        for x in num:
            print(x, end=' ')
        print()
        return
    for i in range(n):
        if check[i] == False:
            if k > 1 and num[-1] < i + 1:
                continue
            num.append(i+1)
            check[i] = True
            back_tracking(num, check, k +1)
            num.pop()
            check[i] = False


n , m = map(int,input().split())
check = [False] * n
num = []
back_tracking(num, check, 0)