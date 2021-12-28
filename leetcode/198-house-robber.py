from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        maximum = 0

        if len(nums) == 0:
            return maximum

        if len(nums) == 1:
            return nums[0]

        dp = [0 for x in range(len(nums))]

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = nums[1]
            elif i == 2:
                dp[i] = nums[i]+dp[i-2]
            else:
                dp[i] = max(nums[i]+dp[i-2], nums[i]+dp[i-3])

            maximum = max(dp[i], dp[i-1])

        return maximum