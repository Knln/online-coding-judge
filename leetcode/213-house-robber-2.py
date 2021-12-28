from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        maximum = 0

        if len(nums) == 0:
            return maximum
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0 for x in range(len(nums))]
        dp2 = [0 for x in range(len(nums))]

        for i in range(0, len(nums)-1):
            # Check if we loop around
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            maximum = max(maximum, dp[i])

        for i in range(1, len(nums)):
            dp2[i] = max(nums[i]+dp2[i-2], dp2[i-1])
            maximum = max(maximum, dp2[i])

        return maximum


sol = Solution()