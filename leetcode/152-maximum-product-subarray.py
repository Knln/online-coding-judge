from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        absolute_maximum = 0

        for i, num in enumerate(nums):
            index = i+1
            local_maximum, sum = num, num

            while index != len(nums):
                sum = sum*nums[index]
                local_maximum = max(local_maximum, sum)
                index += 1

            absolute_maximum = max(local_maximum, absolute_maximum)

        return absolute_maximum

solution = Solution()
print(solution.maxProduct(nums=[2,3,-2,4]))
print(solution.maxProduct(nums=[-2,0,-1]))
print(solution.maxProduct(nums=[-2,1,-1]))
