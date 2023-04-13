def getDivisor(n):
    count = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count
            
def solution(e, starts):
    result = []
    divisor = [1 for _ in range(e+1)]
    memo = 0
    starts_dict = {}
    sorted_starts = sorted(starts)

    for i in range(2, e+1):
        for j in range(i, e+1, i):
            divisor[j] += 1
    
    for i in range(len(sorted_starts)):
        if memo == 0:
            max_index = divisor[sorted_starts[i]:].index(max(divisor[sorted_starts[i]:]))+sorted_starts[i]
            starts_dict[sorted_starts[i]] = max_index
            memo = max_index
        else:
            if sorted_starts[i] <= memo:
                starts_dict[sorted_starts[i]] = memo
            else:
                memo = divisor[sorted_starts[i]:].index(max(divisor[sorted_starts[i]:]))+sorted_starts[i]
                starts_dict[sorted_starts[i]] = memo
    
    for s in starts:
        result.append(starts_dict.get(s))
        
    return result