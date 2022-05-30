class Solution:
    def reverse(self, x: int) -> int:
        max_num = pow(2,31) - 1
        min_num = -pow(2,31)
        s = str(x)
        if x < 0:
            s = s.replace('-',"")
            s = s[::-1]
            if -int(s) < min_num:
                return 0
            return -int(s)
        else:
            s = s[::-1]
            if int(s) >= max_num:
                return 0
            return int(s)



sol = Solution()
print(sol.reverse(1534236469))