"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        transposed = zip(*strs)
        prefix = ""

        for row in transposed:
            temp_letter = ""
            for i, letter in enumerate(row):
                if i == 0:
                    temp_letter = letter
                elif temp_letter != letter:
                    return prefix
                else:
                    continue
            prefix = prefix + temp_letter

        return prefix


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.longestCommonPrefix(["flower", "flow", "flight"])))
    print("{}".format(solution.longestCommonPrefix(["dog", "racecar", "car"])))
