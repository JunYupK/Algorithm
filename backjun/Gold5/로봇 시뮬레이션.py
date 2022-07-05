a, b = map(int,input().split())
board = [[0] * a for _ in range(b)]
n, m = map(int,input().split())
robot = []
for _ in range(n):
    robot.append(list(map(str,input().split())))
