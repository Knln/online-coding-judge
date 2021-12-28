from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dictionary = defaultdict(int)
        answer = set()

        for element in nums:

            dictionary[element] += 1

            if dictionary[element] > len(nums) // 2:
                return element

        return 0

solution = Solution()
print(solution.majorityElement(nums = [3,2,3]))