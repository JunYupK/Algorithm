from collections import deque
class Solution:
    def trap(self, height):
        if len(height) < 1:
            return 0
        left = 0
        right = len(height) - 1
        maxleft = height[left]
        maxright = height[right]
        result = 0
        while left <= right:
            if maxleft <= maxright:
                maxleft = max(maxleft, height[left])
                result += maxleft - height[left]
                left += 1
            else:
                maxright = max(maxright,height[right])
                result += maxright - height[right]
                right -= 1
        print(result)
        return result
sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol.trap(height)