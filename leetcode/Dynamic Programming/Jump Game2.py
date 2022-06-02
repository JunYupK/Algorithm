class Solution:
    def jump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return 0
        dp = [0] * len(nums)
        count = [0] * len(nums)
        dp[0] = nums[0]
        count[0] = 1


sol = Solution()
nums = [3, 2, 1]
print(sol.jump(nums))