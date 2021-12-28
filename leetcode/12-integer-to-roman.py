class Solution:
    def intToRoman(self, num: int) -> str:

        roman_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
                      10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        """
        DP Takes too long
        minInt = [0] * (num+1)
        used = [0] * (num+1)

        if num in roman_dict.keys():
            return roman_dict.get(num)
        else:
            for n in range(num+1):  # Range from 0 to number
                minLetters = n
                newInteger = 1
                for j in [k for k in roman_dict.keys() if k <= n]:
                    if minInt[n-j] < minLetters:
                        minLetters = minInt[n-j] + 1
                        newInteger = j
                minInt[n] = minLetters
                used[n] = newInteger
        """
        roman_numeral = ""
        highest_num = 0

        while num > 0:
            for k, v in roman_dict.items():
                if k <= num:
                    roman_numeral += v
                    num -= k
                    break

        return roman_numeral


if __name__ == '__main__':
    solution = Solution()
    print("{}".format(solution.intToRoman(1)))
    print("{}".format(solution.intToRoman(3)))
    print("{}".format(solution.intToRoman(4)))
    print("{}".format(solution.intToRoman(8)))
    print("{}".format(solution.intToRoman(9)))
    print("{}".format(solution.intToRoman(49)))
    print("{}".format(solution.intToRoman(58)))
    print("{}".format(solution.intToRoman(1994)))
