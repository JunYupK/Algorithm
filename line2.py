from collections import deque
#가입기간 & 연간 납부기간
#90만원 이상 2년이상 24 >=
#60만원 이상 5년 이상 60 >=
def solution(periods, payments, estimates):
    answer = [0, 0]
    count1 , count2 = 0, 0
    for i, p in enumerate(periods):
        q = deque(payments[i])
        present = sum(q)
        q.popleft()
        future = sum(q)
        future += estimates[i]
        #일반 -> vip
        #60만원 이상 90만원 미만인데 기간이 5년이 된경우
        if 600000 <= present < 900000 and p == 59:
            answer[0] += 1
        #90만원씩 냈는데 기간이 2년이 된경우
        elif p == 23 and future >= 900000:
            answer[0] += 1
        #2년이상 5년미만인데 90만원이상 낸 경우 90만원 미만이였는데
        elif 24 <= p < 60 and present < 900000 and future >= 900000:
            answer[0] += 1
        #5년이상인데 60만원 이상 된 경우 현재는 60만원 이하
        elif p >= 60 and present < 600000 and future >= 600000:
            answer[0] += 1


        #vip -> 일반
        #기간은 무조건 24개월 이상임!
        #2년이상 5년미만인데 90만원 이상 안낸 경우
        if 24 <= p < 59 and present >= 900000 and future < 900000:
            answer[1] += 1
        # 단 딱 5년이 되는데 60만원 이상 90만원 이하인 경우는 상관 x 즉 24개월이상 ~ 58개월 이하
        # 그런데 59개월에서 60만원 이하인경우도 체크
        elif p == 59 and present >= 900000 and future <600000:
            answer[1] += 1
        #5년 이상인데 60만원 이상 안낸경우
        elif p >= 60 and present >= 600000 and future < 600000:
            answer[1] += 1
    print(answer)
    return answer

periods = [24, 59, 59, 60]
payments =[[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]
estimates = [350000, 50000, 40000, 50000]
solution(periods, payments, estimates)
