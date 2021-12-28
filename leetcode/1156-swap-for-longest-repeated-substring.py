class Solution:
    def maxRepOpt1(self, text: str) -> int:

        if len(text) == 1:
            return 1

        longest_substring_index = []
        longest_substring = 1
        substring = 1

        # identify repeating characters
        # get total count of one char
        # find another a to replace b to increase by maxlen+1
        # OR find another a to replace middle char len(b) == 1 and make sure the left and right side are the same


        return 0

solution = Solution()
print(solution.maxRepOpt1(text="ababa"))
print(solution.maxRepOpt1(text="aaabbbabbaaa"))
print(solution.maxRepOpt1(text="aaaabbaaa"))