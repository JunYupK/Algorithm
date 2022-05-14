from collections import deque
def find_parent(edge, tree):
    for i,j,cost in tree:
        if i == edge:
            find_parent(i, tree)
        elif j == edge:
            find_parent(j , tree)

    return edge
def solution(n, costs):
    answer = 0
    edges = [False] * n
    costs = sorted(costs, key=lambda x:x[2])
    minimum_tree = []
    for i, j, cost in costs:
        if edges[i] == False and edges[j] == False:
            minimum_tree.append([i,j,cost])
            minimum_tree.append([j,i, cost])
            edges[i] = True
            edges[j] = True
        elif edges[i] == False:
            if find_parent(i,minimum_tree) != find_parent(j,minimum_tree):
                minimum_tree.append([i,j,cost])
                edges[j] = True
        elif edges[j] == False:
            if find_parent(i,minimum_tree) != find_parent(j,minimum_tree):
                minimum_tree.append([j,i,cost])
                edges[i] = True
    print(minimum_tree)
    return sum(edges)

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(4, costs)