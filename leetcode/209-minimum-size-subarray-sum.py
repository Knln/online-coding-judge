from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        min_subarray = float('inf')
        left, right, summ = 0, 0, 0

        while right < len(nums):
            summ += nums[right]
            while summ >= s:
                min_subarray = min(min_subarray, right - left + 1)
                summ -= nums[left]
                left += 1

            right += 1

        if min_subarray == float('inf'):
            return 0
        else:
            return int(min_subarray)

solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))