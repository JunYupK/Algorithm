from itertools import permutations,combinations
#소수 판별 함수
def is_prime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    for i in range(2, num-1):
        if num % i == 0:
            return False
        i += 1
    return True
def solution(numbers):
    answer = 0
    tmp = set()
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            tmp.add(int("".join(num)))
    for num in tmp:
        if is_prime(num) is True:
            answer += 1
    return answer

numbers = "011"
solution(numbers)

#소수 판별 부분에서는 효율성 관련 부분을 위해 에라토스테네스의 체를 이용하여 효율성을 끌어올릴 수 있으며, 순열과 조합의 차이를 더
#극명하게 유연하게 다루도록 생각을 해보자