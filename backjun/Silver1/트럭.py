from collections import deque
n, w, l = map(int,input().split())
truck = list(map(int,input().split()))
bridge = deque()
truck = deque(truck)
time = 0
bridge_w = 0
while bridge or truck:
    time += 1
    if len(bridge) != 0 and time - bridge[0][0] == w:
        t_time, t_w = bridge.popleft()
        bridge_w -= t_w
    if len(truck) != 0 and bridge_w + truck[0] <= l:
        bridge.append((time, truck[0]))
        bridge_w += truck.popleft()
print(time)