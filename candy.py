from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest_candy_num = max(candies)
        return_array = []
        for candy in candies:
            if  candy + extraCandies >= largest_candy_num :
                return_array.append(True)
            else:
                return_array.append(False)
        return return_array


solution = Solution()


candies = [4,2,1,1,2]

print(solution.kidsWithCandies(candies,1))
