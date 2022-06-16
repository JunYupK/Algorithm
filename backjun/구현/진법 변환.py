n, b = input().split()
b = int(b)
n = list(n)
n = n[::-1]
result = 0
num = 1
for char in n:
    if char.isalpha() is False:
        result += int(char) * num
    else:
        char = ord(char) - 55
        result += char * num
    num *= b

print(result)