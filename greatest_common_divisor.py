from typing import List
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0:len(str2)] != str2:
            return ""
        else:
            if str1 == str2:
                return str1
            else:
                return self.gcdOfStrings(str1, str2[0:len(str2)])
    
solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
print(solution.gcdOfStrings(str1, str2))
