from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        string_pointer, word_pointer = 0,0
        longest_word = ""
        longest_word_len = 0

        if not d or not s:
            return ""

        for word in d:

            while word_pointer < len(word) and string_pointer < len(s):
                if word[word_pointer] == s[string_pointer]:
                    string_pointer += 1
                    word_pointer += 1
                else:
                    string_pointer += 1

            if word_pointer == len(word) and longest_word_len <= len(word):
                if not longest_word:
                    longest_word = word

                if len(longest_word) < len(word):
                    longest_word = word
                else:
                    if word < longest_word:
                        longest_word = word

                longest_word_len = len(word)

            word_pointer, string_pointer = 0, 0

        return longest_word


solution = Solution()
print(solution.findLongestWord(s="abpcplea", d=["ale","apple","monkey","plea"]))