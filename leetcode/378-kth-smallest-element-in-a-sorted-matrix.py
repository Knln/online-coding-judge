from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for row in matrix:
            l += row
        return sorted(l)[k-1]

solution = Solution()
solution.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8)