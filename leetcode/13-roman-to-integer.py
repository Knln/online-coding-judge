"""
Example 1:
Input: "III"
Output: 3
Example 2:
Input: "IV"
Output: 4
Example 3:
Input: "IX"
Output: 9
Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        roman_dict = dict()
        roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        prev_char_int = 9999
        roman_int = 0

        for index, char in enumerate(s):
            char_int = roman_dict.get(char)
            if prev_char_int < char_int:
                result = char_int - prev_char_int - prev_char_int
                prev_char_int = 9999
            else:
                prev_char_int = char_int
                result = char_int

            roman_int += result

        return roman_int


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.romanToInt("III")))
    print("{}".format(solution.romanToInt("IV")))
    print("{}".format(solution.romanToInt("IX")))
    print("{}".format(solution.romanToInt("LVIII")))
    print("{}".format(solution.romanToInt("XLIV")))
    print("{}".format(solution.romanToInt("MCMXCIV")))
    print("{}".format(solution.romanToInt("MM")))
    print("{}".format(solution.romanToInt("I")))
