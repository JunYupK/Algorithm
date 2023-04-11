def solution(number, limit, power):
    answer = 0
    dmg = []
    def count_measure(n):
        if n == 1:
            return 1
        count = 0
        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0: 
                count += 1
                if i ** 2 != n:
                    count += 1
        return count
    for i in range(1, number+1):
        dmg.append(count_measure(i))
    for d in dmg:
        if limit >= d:
            answer += d
        else:
            answer += power
    return answer