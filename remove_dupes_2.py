from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        nums.sort()
        while i < len(nums)-2:
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                nums.remove(nums[i])
                i = i - 1
            i = i + 1
        return len(nums)


solution = Solution()
nums = [1,1,1,2,2,3]
print(solution.removeDuplicates(nums))
print(nums)