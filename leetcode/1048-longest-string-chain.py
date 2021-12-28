from typing import List
from collections import defaultdict

# This solution looks from the word with the most letters and adds it to the dp
# e.g. for xb and xbc it will first try b, then x --> then bc, xc, bc. It finds bc in the dictionary
# and then adds the dp[index_of_xb] + 1 or keeps it dp[i]
# It needs to do this just in case of like xbcd bcd cd d and xbc. xbc will only have 1 ofc
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        word_dict = defaultdict(int)
        for w in words:
            for l in w:
                word_dict[l] += 1

        lookup_dict = {word: i for i, word in enumerate(words)}
        dp = [1] * len(words)
        max_length = 1

        for i, w in enumerate(words):
            for j, l in enumerate(w):

                temp = words[i][0:j] + words[i][j+1:]
                print(temp)
                if temp in lookup_dict:
                    dp[i] = max(dp[i], dp[lookup_dict[temp]] + 1)

                max_length = max(dp[i], max_length)

        return max_length


solution = Solution()
print(solution.longestStrChain(words = ["a","b","ba","bca","bda","bdca"]))
print(solution.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc", "dixcb"]))
