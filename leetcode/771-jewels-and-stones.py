from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels_dictionary = {k: 0 for k in jewels}
        counter = 0

        for s in stones:
            if jewels_dictionary[s]:
                counter += 1

        return counter

solution = Solution()
print(solution.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))