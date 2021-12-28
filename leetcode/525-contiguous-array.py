from collections import defaultdict
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_length = 0
        count = 0
        seen = {0: -1}

        for i, number in enumerate(nums):
            if number == 1:
                count += 1
            else:
                count -= 1

            if count in seen:
                max_length = max(i - seen[count], max_length)
            else:
                seen[count] = i

        return max_length

solution = Solution()
print(solution.findMaxLength(nums=[0,1,0]))
print(solution.findMaxLength(nums=[0,0,0,0,1,1]))