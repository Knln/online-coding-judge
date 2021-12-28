from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []
        results.append([])

        if not nums:
            return results

        left, right = 0, 0

        for n in nums:
            l = len(results)
            for i in range(0, l):
                li = results[i]
                results.append(li + [n])

        return results

solution = Solution()
solution.subsets([1,2,3])