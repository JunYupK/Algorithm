from collections import deque


def solution(users, emoticons):
    sales = [10, 20, 30, 40]
    check = [0] * len(emoticons)
    answer = []

    def backtracking(depth):
        if depth == len(emoticons):
            count = 0
            result = 0
            for standard, cost in users:
                sum = 0
                for i in range(len(check)):
                    value = emoticons[i] - int(emoticons[i] * (check[i] / 100))
                    if standard <= check[i]:
                        sum += value
                if sum >= cost:
                    count += 1
                    result -= sum
                result += sum
            answer.append([count, result])
            return
        for i in range(len(sales)):
            check[depth] = sales[i]
            backtracking(depth + 1)
            check[depth] = 0

    backtracking(0)
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer[-1]
