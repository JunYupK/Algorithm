def queens(j):
    global isused1, isused2, isused3, count
    if j == n:
        count += 1
        return
    for i in range(n):
        if isused1[i] or isused2[i+j] or isused3[j-i+ n- 1]:
            continue
        isused1[i] = True
        isused2[i+j] = True
        isused3[j - i + n -1] = True
        queens(j + 1)
        isused1[i] = False
        isused2[i + j] = False
        isused3[j - i + n - 1] = False

global isused1, isused2, isused3, count, n
n = int(input())
count = 0
isused1 = [False] * n
isused2 = [False] * (2 * n)
isused3 = [False] * (n * 2)
board = [[False] * n for _ in range(n)]
queens(0)
print(count)