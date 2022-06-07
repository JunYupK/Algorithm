class Solution:
    def jump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return 0
        dp = [0] * len(nums)
        count = [0] * len(nums)
        dp[0] = nums[0]
        count[0] = 1
        for i in range(1, len(nums)):
            for j in range(i, i+dp[i-1]):
                if nums[j] >= len(nums) - 1:
                    return count[i-1] + 1
            dp[i] = i + nums[i]
            count[i] = count[i-1] + 1



sol = Solution()
nums = [3, 2, 1]
print(sol.jump(nums))