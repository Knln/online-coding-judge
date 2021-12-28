from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl",
                      "6": "mno",
                      "7": "pqrs",
                      "8": "tuv",
                      "9": "wxyz"}
        result = [""]

        for index in range(len(digits)):
            result = [prev + letter for prev in result for letter in phone_dict[digits[index]]]

        return result

if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.letterCombinations("23")))
    print("{}".format(solution.letterCombinations("23456789")))
    print("{}".format(solution.letterCombinations("999")))
    print("{}".format(solution.letterCombinations("98765432")))



