def solution(sizes):
    answer = 0
    big, small = [], []
    for n1, n2 in sizes:
        big.append(max(n1,n2))
        small.append(min(n1,n2))
    return max(big) * max(small)