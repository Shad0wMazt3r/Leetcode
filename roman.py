def romanToInt(s):
        result = 0
        dictionary = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        i = 0
        for character in s:
            if i != len(s) - 1:
                if (dictionary[character] < dictionary[s[i+1]]) :
                    result = result - dictionary[character]
                else:
                    result = result + dictionary[character]
            else:
                result = result + dictionary[character]
            i = i+1
        return result
# print("\nIII",romanToInt("III"))
# print("\nIV",romanToInt("IV"))
# print("\nLVIII",romanToInt("LVIII"))
print("\nMCMXCIV",romanToInt("MCMXCIV"))
