# import sys
# from collections import deque
# sys.setrecursionlimit(10000)
# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         answer = []
#         def is_perfect(data):
#             q = deque()
#             for char in data:
#                 if char == '(':
#                     q.append(char)
#                 else:
#                     if len(q) == 0:
#                         return False
#                     elif q.pop() != '(':
#                         return False
#
#             if len(q) != 0:
#                 return False
#             else:
#                 return True
#
#         def insert_char(n, data, char):
#             data += char
#             if len(data) == n * 2:
#                 if is_perfect(data):
#                     answer.append(data)
#                 return
#             insert_char(n, data, "(")
#             insert_char(n, data, ")")
#         insert_char(n, "", "(")
#         return answer
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.res = []
        self.cur = []
        self.n = n
        self.backtrack(0, 0)
        return self.res

    def backtrack(self, left, right):
        if left > self.n or right > self.n:
            return
        if left + right == 2 * self.n:
            self.res.append("".join(self.cur))
            return

        if left < self.n:
            self.cur.append('(')
            self.backtrack(left + 1, right)
            self.cur.pop()

        if right < left:
            self.cur.append(')')
            self.backtrack(left, right + 1)
            self.cur.pop()
sol = Solution()
print(sol.generateParenthesis(2))