
def solution(sequence):
    answer = 0
    n = len(sequence)
    dp1 = [0] * (len(sequence) + 1)
    dp2 = [0] * (len(sequence) + 1)
    seq1 = [0] * n
    seq2 = [0] * n
    flag = 1
    for i, num in enumerate(sequence):
        seq1[i] = num * flag
        flag *= -1
        seq2[i] = num * flag
    for i in range(1, len(sequence)):
        dp1[i] = max(dp1[i-1]+seq1[i], seq1[i])
        dp2[i] = max(dp2[i-1]+seq2[i], seq2[i])
    return max(max(dp1), max(dp2))

solution([2, 3, -6, 1, 3, -1, 2, 4])