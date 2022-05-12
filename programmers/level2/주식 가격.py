from collections import deque
def solution(prices):
    answer = [0]*len(prices)
    stack = deque()
    for i , price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            num = stack.pop()
            answer[num] = i - num
        stack.append(i)

    while stack:
        num = stack.pop()
        answer[num] = len(prices) - 1 - num
    return answer
prices = [1, 2, 3, 2, 3]
solution(prices)