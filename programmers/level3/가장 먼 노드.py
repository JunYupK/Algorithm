from collections import deque,defaultdict
def solution(n, edge):
    visited = [False] * (n+1)
    answer = 0
    new_edge = []
    adj = defaultdict(list)
    q = deque()
    q.append((1, 0))
    visited[1] = 0
    for i, j in edge:
        adj[i].append(j)
        adj[j].append(i)
    while q:
        data, cost = q.popleft()
        for next in adj[data]:
            if visited[next] is False:
                visited[next] = cost + 1
                q.append((next, cost + 1))
    print(visited)
    num = max(visited)
    return visited.count(num)
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
solution(n,vertex)

# 일반적인 bfs 문제지만 간선의 양방향 기준 1000000개를 넘어가서 단순하게 간선을 for문을 돌리면서 bfs를 구현하면 시간 초과가 뜨는 문제였다.
# defaultdict 를 사용해서 노드와 연결된 다른 노드를 기록해놓고 그 노드를 기준으로 방문 여부를 이용해 bfs 를 구현하면 쉽게 풀리는 문제였다.
# 혼자 최단거리로 삽질하다가 틀린 문제인데 정상적으로 모두 연결되어있는 그래프라면 bfs를 이용하여 방문한 노드를 다시 방문하는 조건이 없는 한
# 1번 기준 노드의 거리는 처음 방문한 경우가 최단 거리로 생각해도 무방하다.