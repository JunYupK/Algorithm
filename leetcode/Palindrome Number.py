class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.replace(' ','')
        max_num = pow(2,31) - 1
        min_num = -pow(2,31)
        if s[0] == '-':
            s= s.replace('-','')
            return -int(s)
        else:
            return int(s)

sol = Solution()
sol.myAtoi("-321")