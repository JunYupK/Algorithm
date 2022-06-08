x = input()
y = input()
def romantoint(a):
    roman = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    stack = []
    stack.append(a[0])
    number = 0
    for i in range(1,len(a)):
        if len(stack) == 0:
            stack.append(a[i])
            continue
        if roman[stack[-1]] == roman[a[i]]:
            stack.append(a[i])
        elif roman[stack[-1]] < roman[a[i]]:
            tmp = stack.pop()
            number += roman[tmp+a[i]]
        else:
            stack.append(a[i])

    while stack:
        tmp = stack.pop()
        number += roman[tmp]
    return number

def inttoroman(num):
    roman = {1000 : 'M', 900:'CM', 500:'D' ,  400:'CD' , 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V',4:'IV',1:'I'}
    answer = ""
    while num != 0:
        for k, v in roman.items():
            if num - k >= 0:
                num -= k
                answer += v
                break
    return answer

result = romantoint(x) + romantoint(y)
print(result)
print(inttoroman(result))
