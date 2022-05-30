class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) -1
        area = 0
        while right - left > 0:
            area = max(area ,(right - left) * min(height[left], height[right]))
            if height[left]>= height[right]:
                right -= 1
            else:
                left += 1
        return area

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
sol.maxArea(height)

#greedy와 투포인터가 섞인 구조라고 볼 수 있다 메인 아이디어는 투포인터