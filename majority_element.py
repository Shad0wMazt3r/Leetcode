from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        majority_length = (n  // 2)
        i = 0
        while i <= majority_length:
            if nums[i] == nums[majority_length+i]:
                return nums[i]
            i = i +1 

solution = Solution()
nums = [3,2,3]
print(solution.majorityElement(nums))