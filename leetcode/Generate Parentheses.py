from collections import deque
from itertools import combinations,permutations
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answer = []
        for i in range(n):
            answer.append('(')
            answer.append(')')
        for com in permutations(answer, n):
            x = 0


sol =Solution()
n = 3
sol.generateParenthesis(8)
