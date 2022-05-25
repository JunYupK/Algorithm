class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        start, length = 0, 0
        for i in range(len(s)):
            if s[i-length: i + 1] == s[i-length:i+1][::-1]:
                start, length = i - length , length + 1
            elif i - length - 1 >= 0 and s[i-length-1:i+1] == s[i - length - 1:i+1][::-1]:
                start, length = i - length - 1 , length + 2

        return s[start:start+length]

sol = Solution()
s = "babad"
sol.longestPalindrome(s)