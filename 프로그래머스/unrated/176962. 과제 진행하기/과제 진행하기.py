from collections import deque
def time_to_min(time):
    hour, mit = time.split(':')
    return int(hour) * 60 + int(mit)
def solution(plans):
    answer = []
    new_plans = []
    stack = []
    for plan in plans:
        tmp = [plan[0], time_to_min(plan[1]), int(plan[2])]
        new_plans.append(tmp)

    new_plans = deque(sorted(new_plans, key=lambda x:x[1]))
    time = 0
    for name, start, cost in new_plans:
        if stack:
            prev_name, prev_start, prev_cost = stack.pop()
            flag = start - prev_start
            if flag < prev_cost:
                stack.append([prev_name, prev_start, prev_cost - flag])
            else:
                answer.append(prev_name)
                flag -= prev_cost
                while stack and flag:
                    prev_name, prev_start, prev_cost = stack.pop()
                    if flag < prev_cost:
                        stack.append([prev_name, prev_start, prev_cost-flag])
                        break
                    else:
                        answer.append(prev_name)
                        flag -= prev_cost
        stack.append([name, start, cost])
    for i in range(len(stack)-1, -1 , -1):
        answer.append(stack[i][0])
    return answer