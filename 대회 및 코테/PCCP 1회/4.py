import heapq
#우선 실행시간기준으로 우선순위 큐 하나 생성
# 실행시간이 지난 경우는 여기서 우선순위를 따져서 실행 후 답 체크
def solution(program):
    answer = [0] * 11
    time_queue = []
    score_queue = []
    time = 0
    for a,b,c in program:
        heapq.heappush(time_queue,(b,a,c))
    while time_queue or score_queue:
        while time_queue:
            if time_queue[0][0] <= time:
                start_time, score, cost = heapq.heappop(time_queue)
                heapq.heappush(score_queue, (score, start_time,cost))
            else:
                break
        if score_queue:
            tmp_score, tmp_start, tmp_cost = heapq.heappop(score_queue)
            answer[tmp_score] += (time - tmp_start)
            time += tmp_cost
        else:
            time += 1
    answer[0] = time
    return answer

solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]])
# 우선순위로만 뽑으면 실행시간이 아닐수도..
# 실행시간과 우선순위를 모두 고려하는 방법?
# 걍 실행시간과 우선순위로 sort를 갈기면 되지않나? << 대기중일땐 어떻게 할래? 이땐 시간말고 우선순위로 다음에 실행할 친구를 정해야 함
# 우선순위 큐의 기준을 그때 그때 바꿀순없고..
# 우선순위 큐를 2개를 둔다면? ex. 보석도둑