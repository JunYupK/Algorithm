# from collections import deque
# from itertools import combinations
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         q1 = deque(s)
#         q2 = deque(p)
#         tmp1 = tmp2 = ''
#         while q1 and q2:
#             char1 = q1.popleft()
#             char2 = q2.popleft()
#             if char2 == '*' and tmp2[-1] == char1:
#                 while q1:
#                     x = q1.popleft()
#                     if x != char1:
#                         q1.insert(0,x)
#                         break
#             elif char1 == char2:
#                 tmp1 += char1
#                 tmp2 += char2
#             else:
#
#         if len(q1) != 0 or len(q2) != 0:
#             return False
#         else:
#             return True
#
#
# sol = Solution()
# s = 'caaaaaaaaa'
# p = 'qa*c'
# print(sol.isMatch(s,p))