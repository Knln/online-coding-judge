from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        original = heights.copy()

        if len(heights) == 1:
            return 0

        for i in range(1, len(heights)):

            curr = heights[i]

            j = i - 1
            while j >= 0 and curr < heights[j]:
                heights[j+1] = heights[j]
                j -= 1

            heights[j+1] = curr

        counter = 0

        for o, h in zip(original, heights):
            if o != h:
                counter += 1

        return counter

solution = Solution()
print(solution.heightChecker([1,1,4,2,1,3]))
print(solution.heightChecker([6,5,4,3,2,1]))
print(solution.heightChecker([1,100]))
print(solution.heightChecker([1,2,3,4,5,6,7]))