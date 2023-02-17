import heapq
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    q = []
    for i in range(n):
        num = numbers[i]
        print(q, answer)
        while q and q[0][0] < num:
            tmp, index = heapq.heappop(q)
            answer[index] = num
        heapq.heappush(q, (num, i))
    return answer
solution([9, 1, 5, 3, 6, 2])