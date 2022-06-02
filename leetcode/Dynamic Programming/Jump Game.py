class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1 ,len(nums)- 1):
            if i > dp[i-1]:
                return False
            dp[i] = max(dp[i-1], i + nums[i])
        if dp[-2] >= len(nums) - 1:
            return True
        else:
            return False

sol = Solution()
nums = [0,2,3]
print(sol.canJump(nums))