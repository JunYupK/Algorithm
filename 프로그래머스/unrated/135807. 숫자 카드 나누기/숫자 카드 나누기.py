from math import gcd
def find_gcd(arr):
    tmp = arr[0]
    for i in range(1,len(arr)):
        tmp = gcd(tmp, arr[i])
    return tmp
def solution(arrayA, arrayB):
    answer1 = 0
    answer2 = 0
    gcdA, gcdB = find_gcd(arrayA), find_gcd(arrayB)
    for num in arrayA:
        if num % gcdB == 0:
            answer1 = 0
            break
        answer1 = max(answer1, gcdB)
    for num in arrayB:
        if num % gcdA == 0:
            answer2 = 0
            break
        answer2 = max(answer2, gcdA)
        
    return max(answer1, answer2)