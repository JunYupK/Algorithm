class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        min_num = 1e9
        tmp = 1e9
        for i in range(1, len(nums)-1):
            left = 0
            right = len(nums) - 1
            answer = []
            while left != right:
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue
                sums = nums[i] + nums[left] + nums[right]
                if sums - target > 0:
                    right -= 1
                elif sums - target < 0:
                    left += 1
                else:
                    tmp = sums
                    break
                if abs(sums - target) < min_num:
                    min_num = abs(sums - target)
                    tmp = sums
        return tmp

sol = Solution()
nums = [0, 0, 0]
target = 1
sol.threeSumClosest(nums, target)

#효율성 망~~