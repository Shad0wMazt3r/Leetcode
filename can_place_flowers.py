from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if len(flowerbed) == 1:
            if n > 1:
                return False
            else:
                if n == 1:
                    if flowerbed[0] == 0:
                        return True
                    else:
                        return False
        while i < len(flowerbed) - 2:
            if i == 0 and not i == len(flowerbed) - 3:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    n = n - 1
            elif i == len(flowerbed) - 3:
                if flowerbed[i + 1] == 0 and flowerbed[i + 2] == 0:
                    n = n - 1 
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                n = n - 1
                i = i + 1
            i = i + 1
        if n <= 0:
            return True
        else:
            return False

solution = Solution()
flowerbed = [1,0,0]
n = 1
print(solution.canPlaceFlowers(flowerbed, n))