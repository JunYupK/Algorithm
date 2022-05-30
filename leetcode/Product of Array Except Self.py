import math
class Solution:
    def productExceptSelf(self, nums):
        result = math.prod(nums)
        answer = []
        for i, n in enumerate(nums):
            if n == 0:
                tmp = nums[:]
                del tmp[i]
                answer.append(math.prod(tmp))
                continue
            answer.append(result//n)
        return answer


sol = Solution()
nums = [-1,1,0,3,-3]
sol.productExceptSelf(nums)