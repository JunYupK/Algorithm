class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.max_rob(nums[1:]), self.max_rob(nums[:-1]))
    def max_rob(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

sol = Solution()
nums = [2,7,9,3,1]
print(nums[1:])
sol.rob(nums)