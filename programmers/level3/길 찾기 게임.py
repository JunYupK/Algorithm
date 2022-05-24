from collections import defaultdict
class Node:
    def __init__(self, num):
        self.left = False
        self.right = False
        self.num = num
def solution(nodeinfo):
    answer = [[]]
    node = defaultdict(list)
    tree = []
    for i ,n in enumerate(nodeinfo):
        node[i+1] = n
    print(node)
    node = sorted(node.items(),key=lambda x:(x[1][1]), reverse=True)
    print(node)
    for i, n, d in enumerate(node):
        x = d[0]
        y = d[1]
        tmp = Node(n)
        if i == 0:
            tree.append(tmp)
            continue
        if y <= node[i-1][1][1] and x < node[i-1][1][0]:
            tree[i-1].left = n
            tree.append(tmp)
        elif y <= node[i-1][1][1] and x > node[i-1][1][0]:
            tree[i-1].right = n
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(nodeinfo)