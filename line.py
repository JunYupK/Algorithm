from collections import defaultdict
def solution(logs):
    answer = []
    user = {}
    problem = defaultdict(list)
    for log in logs:
        log = log.split(" ")
        user[log[0]] = 1
        if problem.get(log[1]) is None:
            problem[log[1]].append(log[0])
        else:
            if log[0] not in problem[log[1]]:
                problem[log[1]].append(log[0])


    for k, v in problem.items():
        if len(v) >= len(user)/2:
            answer.append(k)

    answer.sort()

    return answer

logs = ["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]
solution(logs)