from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        mydict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char == '(' or char == '{' or char == '[':
                q.append(char)
            else:
                if len(q) == 0:
                    return False
                if q.pop() != mydict[char]:
                    return False
        if len(q) != 0:
            return False
        return True

sol =Solution()
s = '()'
print(sol.isValid(s))