# #코드가 전체 주석처리는 다시 풀어볼 문제!
#
# from itertools import combinations
# def solution(relation):
#     row = len(relation)
#     col = len(relation[0])
#     candidates = []
#     for i in range(1, col + 1):
#         candidates.extend(combinations(range(col), i ))
#     unique = []
#     for candi in candidates:
#         tmp = [tuple([item[i] for i in candi]) for item in relation]
#         if len(set(tmp)) == row:
#             unique.append(candi)
#
#     answer = set(unique)
#     print(unique)
#     for i in range(len(unique)):
#         for j in range(i+1, len(unique)):
#             if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
#                 answer.discard(unique[j])
#     print(answer)
#     return len(answer)
#
#
# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# solution(relation)


