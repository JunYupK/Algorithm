class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort(key=lambda x:len(x))
        answer = ""
        for i ,char in enumerate(strs[0]):
            check = True
            for j in range(len(strs)):
                if strs[j][i] != char:
                    check = False
                    break
            if check:
                answer += char
            else:
                return answer
        return answer

sol =Solution()
strs = ["flower","flow","flight"]
sol.longestCommonPrefix(strs)