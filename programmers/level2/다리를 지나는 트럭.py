from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque() #다리큐
    bridge_sum = 0 #현재 다리의 무게
    time = 1
    truck_weights = deque(truck_weights)
    bridge.append([truck_weights[0], time])
    bridge_sum += truck_weights.popleft()
    while  len(bridge) != 0 or len(truck_weights) != 0: #다리와 트럭 큐가 모두 비어야 모두 건넌것
        time += 1 #시간
        if time - bridge[0][1] == bridge_length: #현재 큐의 맨앞의 트럭이 다리를 건너기 시작한 시간과 현재시간의 차이가 다리의 길이와 같으면 pop
            num = bridge.popleft()
            bridge_sum -= num[0]
        if len(truck_weights) != 0:
            truck  = truck_weights[0]
            if bridge_sum + truck <= weight:
                bridge.append([truck , time])
                bridge_sum += truck
                truck_weights.popleft()
    return time

bridge_length = 100
weight = 100
truck_weight = [10,10,10,10,10,10,10,10,10]
solution(bridge_length,weight,truck_weight)

#다리에 트럭이 동시에 오를 수 없다는 점을 이용했다. 다리위에 트럭이 여러대 연속으로 들어가도 무조건 시간차이는 나기 때문에
# 다리의 무게 큐에 트럭이 다리에 오르는 시간을 같이 올린 후 맨 앞에 있는 트럭의 오른시간과 현재 시간의 차이가 다리의 길이와 같으면 다리를 건넌 것으로 판단하고
# 다리 큐에서 트럭을 뺴주었다
