from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,n):
            del nums1[-1]
        for num in nums2:
            nums1.append(num)
        nums1.sort()

solution = Solution()
nums1=[1,2,3,0,0,0]
solution.merge(nums1, 6, [4,5,6], 3)
print(nums1)