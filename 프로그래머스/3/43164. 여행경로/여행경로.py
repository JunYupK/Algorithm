from collections import deque, defaultdict
global ans
ans = []
def dfs(tickets, visited, depth, route):
    global ans
    if depth == len(tickets):
        ans.append(route)
    
    for i, next_pos in enumerate(tickets):
        left, right = next_pos
        last = route[-1]
        tmp = route[:]
        tmp.append(right)
        if left == last and visited[i] is False:
            visited[i] = True
            dfs(tickets, visited, depth + 1, tmp)
            visited[i] = False
    return route    
    
def solution(tickets):
    global ans
    visited = [False] * len(tickets)
    tickets.sort()
    dfs(tickets, visited, 0, ["ICN"])
    ans.sort()
    return ans[0]
