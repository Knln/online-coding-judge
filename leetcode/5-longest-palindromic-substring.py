"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not isinstance(s, str) or s == '':
            return ''

        matrix = [[False for i in range(len(s))] for j in range(len(s))]
        longest = 1
        longest_string = s[0]

        for i in range(len(s)):
            matrix[i][i] = True

        for start in range(len(s)-1, -1, -1):
            for end in range(start+1, len(s)):
                print(end)

                if s[start] == s[end]:
                    if end - start == 1 or matrix[start+1][end-1]:
                        matrix[start][end] = True
                        if max(longest, end-start+1) != longest:
                            longest_string = s[start:end+1]
                            longest = max(longest, end - start + 1)
        return longest_string

if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.longestPalindrome('abacdfgababa')))