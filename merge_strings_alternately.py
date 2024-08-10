class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        x = 0
        y = 0
        merged = []
        while i < len(word1) + len(word2):
            if i % 2 == 0 and x<len(word1):
                merged.append(word1[x])
                x = x+1
            elif i%2 == 1 and y<len(word2):
                merged.append(word2[y])
                y = y+1
            elif i % 2 == 0 and x>=len(word1):
                merged.append(word2[y])
                y = y+1
            elif i % 2 == 1 and y>=len(word2):
                merged.append(word1[x])
                x = x+1
            else:
                pass
            i = i + 1
        return ''.join(merged)

solution = Solution()
print(solution.mergeAlternately("abcd", "pq"))