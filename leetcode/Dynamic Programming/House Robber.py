class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            print(i)
            print(dp)
            self.maxRob(i, nums, dp)
        return dp[-1]

    def maxRob(self, i, nums, dp):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])


sol = Solution()
nums = [2,7,9,3,1]
print(sol.rob(nums))