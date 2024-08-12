class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(" ")[::-1]
        return " ".join([y for y in x if y])

solution = Solution()

print(solution.reverseWords("  hello world  "))
