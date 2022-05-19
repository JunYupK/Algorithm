from itertools import combinations
def is_prime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eratoss(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]
def solution(nums):
    answer = 0
    numbers = []
    for com in combinations(nums, 3):
        numbers.append(sum(com))
    prime_list = eratoss(max(numbers))
    for n in numbers:
        if n in prime_list:
            answer += 1
    return answer
nums = [1,2,7,6,4]
solution(nums)