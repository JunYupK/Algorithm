from bisect import bisect_left
from collections import deque
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        q = deque(nums1)
        for num in nums2:
            index = bisect_left(q, num)
            q.insert(index, num)

        if len(q) % 2 == 0:
            j = int((n+m) / 2)
            i = j - 1
            answer = (q[i] + q[j]) / 2
        else:
            answer = q[(n+m)//2]
        return answer
nums1 = [1,2]
nums2 = [3,4]
sol =Solution()
print(sol.findMedianSortedArrays(nums1, nums2))