from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        dictionary = defaultdict(int)
        answer = set()

        for element in nums:

            dictionary[element] += 1

            if dictionary[element] > len(nums) // 3:
                answer.add(element)

        return list(answer)

solution = Solution()
print(solution.majorityElement(nums = [3,2,3]))