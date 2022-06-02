class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        nums.sort()
        numDict = {}
        for n in nums:
            if numDict.get(n) is None:
                numDict[n] = 1
            else:
                numDict[n] += 1
        nums = list(set(nums))
        dp = [0] * len(nums)
        dp[0] = nums[0] * numDict[nums[0]]
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                if i > 1:
                    dp[i] = max(nums[i] * numDict[nums[i]] + dp[i-2], dp[i - 1])
                else:
                    dp[i] = max(nums[i] * numDict[nums[i]], dp[i - 1])
            else:
                dp[i] = nums[i] * numDict[nums[i]] + dp[i - 1]
            print(dp)
        return dp[-1]

sol = Solution()
nums = [1,1,1,2,4,5,5,5,6]
sol.deleteAndEarn(nums)