# 라인을 체크 같은 행이나 열에 걸리는 경우는 라인 단 점이 하나만 같은경우는 포인트
# 페이스의 경우 점이 단 하나라도 다른 사각형 범위안에 들어갈 경우 페이스
# 위 모든 경우에 해당 안하면 널
rectangle = []
for _ in range(2):
    x1,y1,x2,y2 = map(int,input().split())
    rectangle.append([(x1,y1),(x2,y2)])

rec_A = rectangle[0]
rec_B = rectangle[1]

if rec_A[0][0] == rec_B[1][0] or rec_A[1][0] == rec_B[0][0]:
    if rec_A[0][1] == rec_B[1][1] or rec_A[1][1] == rec_B[0][1]:
        print("POINT")
    elif (rec_A[1][1] - rec_A[0][1]) +  (rec_B[1][1] - rec_B[0][1]) > max(rec_B[1][1]-rec_A[0][1], rec_A[1][1] - rec_B[0][1]):
        print("LINE")
    else:
        print("NULL")

elif (rec_A[1][0] - rec_A[0][0]) + (rec_B[1][0] - rec_B[0][0]) > max(rec_B[1][0]-rec_A[0][0], rec_A[0][0] - rec_B[1][0]):
    if rec_A[0][1] == rec_B[1][1] or rec_A[1][1] == rec_B[0][1]:
        print("LINE")
    elif (rec_A[1][1] - rec_A[0][1]) + (rec_B[1][1] - rec_B[0][1]) >  max(rec_B[1][1] - rec_A[0][1] , rec_A[1][1] - rec_B[0][1]):
        print("FACE")
    else:
        print("NULL")
else:
    print("NULL")



