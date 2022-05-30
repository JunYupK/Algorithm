class Solution:
    def tribonacci(self, n: int) -> int:
        sol = [0, 1, 1]
        for i in range(3,n+1):
            sol.insert(i, sol[i-1] + sol[i-2] + sol[i - 3])
        return sol[n]

sol = Solution()
sol.tribonacci(10)