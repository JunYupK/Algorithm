king, stone, N = input().split()
N = int(N)
alphaToNum = {'A' : 0, 'B' : 1, 'C':2, 'D': 3, 'E': 4, 'F' : 5, 'G':6, 'H':7 }
numToAlpha = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
moves = {'R': (0, 1), 'L':(0, -1), 'B':(-1,0), 'T':(1,0), 'RT':(1,1), 'LT':(1,-1), 'RB':(-1,1),'LB':(-1,-1)}
king_x, king_y = int(king[1]) - 1 , alphaToNum[king[0]]
stone_x, stone_y = int(stone[1]) - 1, alphaToNum[stone[0]]
for _ in range(N):
    order = input()
    dx, dy = moves[order]
    next_x, next_y = dx + king_x, dy + king_y
    if 0 <= next_x < 8 and 0 <= next_y < 8:
        if next_x == stone_x and next_y == stone_y:
            next_stone_x, next_stone_y = stone_x + dx, stone_y + dy
            if 0 <= next_stone_x < 8 and 0 <= next_stone_y < 8:
                stone_x, stone_y = next_stone_x, next_stone_y
                king_x, king_y = next_x, next_y
            else:
                continue
        else:
            king_x, king_y = next_x, next_y

print(str(numToAlpha[king_y]) + str(king_x+1))
print(str(numToAlpha[stone_y]) + str(stone_x+1))
