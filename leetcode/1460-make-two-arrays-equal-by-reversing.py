from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        if len(target) != len(arr):
            return False

        tracking = {x: 0 for x in range(len(target))}
        found = 0

        for i, element in enumerate(arr):
            for j, element_j in enumerate(target):
                if element == element_j and tracking[j] == 0:
                    tracking[j] = 1
                    found = 1
                    break
            if found != 1:
                return False
            found = 0

        return True

solution = Solution()
print(solution.canBeEqual(target = [1,1,1,1,1], arr = [1,1,1,1,1]))
print(solution.canBeEqual(target = [1,1,1,1,1], arr = [1,1,1,1,2]))