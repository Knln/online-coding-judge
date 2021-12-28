from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []

        length = len(p)
        dictionary = defaultdict(int)
        ordered_dict = defaultdict(int)
        answer  = []

        for k in range(0, length):
            dictionary[p[k]] += 1

        for j in range(0, length-1):
            ordered_dict[s[j]] += 1

        for i in range(length-1, len(s)):
            ordered_dict[s[i]] += 1

            if ordered_dict == dictionary:
                answer.append(i-length+1)
            ordered_dict[s[i-length+1]] -= 1

            if ordered_dict[s[i-length+1]] == 0:
                del ordered_dict[s[i-length+1]]

        return answer

solution = Solution()
print(solution.findAnagrams(s="cbaebabacd",p="abc"))