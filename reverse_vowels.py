from typing import List
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        vowels_indexes = []
        vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i = 0
        for element in s:
            if element in vowels_list:
                vowels.append(element)
                vowels_indexes.append(i)
            i = i + 1
        i = len(vowels_indexes)
        x = list(s)
        for index in vowels_indexes:
            x[index] = vowels[i - 1]
            i = i - 1
        return ''.join(str(y) for y in x)
    
solution = Solution()
string = "leetcode"
print(solution.reverseVowels(string))