"""
Given a string, find the first non-repeating character in it
and return it's index. If it doesn't exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        ordered_dict = dict()

        for char in s:
            if char in ordered_dict.keys():
                ordered_dict[char] += 1
            else:
                ordered_dict[char] = 1

        for idx, letter in enumerate(s):
            if ordered_dict[letter] == 1:
                return idx

        return -1


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.firstUniqChar('leetcode')))
    print("{}".format(solution.firstUniqChar('dddccdbba')))
