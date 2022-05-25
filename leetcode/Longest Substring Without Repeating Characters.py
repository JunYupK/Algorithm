from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s):
        q = deque()
        answer = []
        for char in s:
            if len(q) == 0:
                q.append(char)
                continue
            if char in q:
                answer.append("".join(q))
                while char in q:
                    end = q.index(char)
                    for _ in range(end+1):
                        q.popleft()
                q.append(char)
            else:
                q.append(char)
        answer.append("".join(q))
        answer.sort(key=lambda x:len(x), reverse=True)
        print(answer)
        return len(answer[0])

sol =Solution()
s = "dvdf"
sol.lengthOfLongestSubstring(s)
