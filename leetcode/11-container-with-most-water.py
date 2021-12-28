"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        if not height:
            return 0

        i, max_area = 0, 0
        left = 0
        right = len(height)-1

        while left != right:
            if height[left] > height[right]:
                area = height[right] * (right-left)
                right = right - 1
            elif height[right] > height[left]:
                area = height[left] * (right-left)
                left = left + 1
            else:
                area = height[left] * (right-left)
                left = left + 1

            if area > max_area:
                max_area = area

        return max_area


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])))  # 49
    print("{}".format(solution.maxArea([1, 8])))  # 1
    print("{}".format(solution.maxArea([1])))  # 0
    print("{}".format(solution.maxArea([0, 0])))  # 0
    print("{}".format(solution.maxArea([0])))  # 0
    print("{}".format(solution.maxArea([1, 1, 1, 1])))  # 4
    print("{}".format(solution.maxArea([9, 8, 7, 6, 5, 4, 3, 2, 1])))  # 20
    print("{}".format(solution.maxArea([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])))  # 20
    print("{}".format(solution.maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9])))  # 20
