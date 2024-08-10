from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix  = strs[0]
        i = 0
        for string in strs:
            if i != 0:
                j = 0
                
                for j in range(0, len(string)):
                    if string[j] != prefix[j]:
                        prefix = prefix[:-j]
                        break
            i += 1
        return prefix
solution = Solution()
print(solution.longestCommonPrefix(strs=["flower","flow","flight"]))
