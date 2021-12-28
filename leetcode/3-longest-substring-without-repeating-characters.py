from collections import defaultdict
from collections import OrderedDict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dictionary = OrderedDict()
        longest_string = ""
        len_string = 0

        for char in s:
            if char in dictionary.keys():

                while dictionary:
                    popped_char = dictionary.popitem(last=False)
                    if popped_char[0] == char:
                        break

                longest_string = "".join([k for k, v in dictionary.items()]) + char
            else:
                longest_string = longest_string + char

            len_string = max(len_string, len(longest_string))
            dictionary[char] = 1

        return len_string


solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))
print(solution.lengthOfLongestSubstring("bbbb"))
print(solution.lengthOfLongestSubstring("pwwkwkew"))
print(solution.lengthOfLongestSubstring(""))
