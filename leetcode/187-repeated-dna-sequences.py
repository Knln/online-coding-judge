from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        if len(s) <= 10:
            return []

        tracking = defaultdict(int)
        tracking[s[0:10]] = 1

        answer = set()

        for i in range(10, len(s)):
            if s[i-9:i+1] in tracking:
                answer.add(s[i-9:i+1])
            else:
                tracking[s[i-9:i+1]] = 1

        return list(answer)

solution = Solution()
print(solution.findRepeatedDnaSequences(s="CAAAAAAAAAC"))