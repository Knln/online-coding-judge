from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1 = Counter(nums1)
        answer = []

        for element in nums2:
            if c1[element] > 0:
                answer.append(element)
                c1[element] -= 1

        return answer

solution = Solution()
print(solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))