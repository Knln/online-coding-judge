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

        matrix = [[None for i in range(len(s))] for j in range(len(s))]

        for j in range(len(s)):
            for i in range(j, len(s)):
                print(i)
                if i == j:
                    matrix[i][j] = True
                elif i-1 == j:
                    matrix[i][j] = (s[i] == s[j])
                else:
                    matrix[i][j] = (matrix[j+1][i-1] and s[i] == s[j])
        print(matrix)

        return ''
if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.longestPalindrome('abacdfgdcaba')))
