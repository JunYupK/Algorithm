from bisect import bisect_left
class Solution:
    def threeSum(self, nums):
        answer = []
        nums.sort()
        print(nums)
        start = 0
        end = len(nums) -1
        while start <= end:
            sum_num = nums[start] + nums[end]
            tmp = nums[start+1:end]
            if sum_num <= 0:
                index = bisect_left(tmp, -sum_num)
                if index > len(tmp)-1 or index < 0:
                    start += 1
                    continue
                if tmp[index] + sum_num == 0 and [nums[start], tmp[index], nums[end]] not in answer:
                    answer.append([nums[start], tmp[index], nums[end]])
                start += 1
            else:
                index = bisect_left(tmp, -sum_num)
                if index < 0 or index > len(tmp) -1 :
                    end -= 1
                    continue
                if tmp[index] + sum_num == 0 and [nums[start], tmp[index], nums[end]] not in answer:
                    answer.append([nums[start], tmp[index], nums[end]])
                end -= 1
        print(answer)
        return answer

sol = Solution()
nums = [-1,0,1,2,-1,-4]
sol.threeSum(nums)

#미해결