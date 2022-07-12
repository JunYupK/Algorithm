n = int(input())

tree = [list(map(int,input()))for _ in range(n)]
result = []

def quad_tree(x, y, n):
    global result
    color = tree[x][y]

    for i in range(x, x+n):
        for j in range(y, y + n):
            if color != tree[i][j]:
                result.append('(')
                quad_tree(x,y,n//2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                result.append(")")
                return
    result.append(color)
quad_tree(0,0,n)
print("".join(map(str,(result))))
