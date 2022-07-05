def make_num(n):
    result = 0
    for char in str(n):
        result += int(char)
    result += n
    return result
n = int(input())
tmp = n
answer = 0
while tmp != 0:
    tmp -= 1
    if make_num(tmp) == n:
        answer = tmp

print(answer)