import sys
import math

input = sys.stdin.readline


# O(log N) 거듭제곱 알고리즘
def power(a, n):
    if n == 0:
        return 1

    x = power(a, n // 2) % FLAG

    # x가 짝수
    if n % 2 == 0:
        return x * x % FLAG

    # x가 홀수
    else:
        return x * x * a % FLAG


# 초기 조건
FLAG = 1000000007
sum = 0
dice = int(input())
for i in range(dice):
    n, s = map(int, input().split())
    a = s // math.gcd(n, s)
    b = n // math.gcd(n, s)

    b_inverse = power(b, FLAG - 2) % FLAG
    sum += (a * b_inverse) % FLAG
    sum %= FLAG

# 정답 출력
answer = sum
print(answer)