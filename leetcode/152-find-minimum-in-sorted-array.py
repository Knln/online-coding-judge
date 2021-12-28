from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        l = nums[0]
        r = nums[len(nums)-1]
        x = 0
        y = len(nums)-1
        answer = l

        while l > r:

            m = x + (y-x) // 2

            if nums[m] < l:
                r = nums[m]
                y = m
            elif nums[m] > l:
                l = nums[m]
                x = m
            else:
                return nums[m+1]

        return answer

solution = Solution()

print(solution.findMin(nums=[11,13,15,17]))
print(solution.findMin(nums=[4,5,6,7,0,1,2]))
print(solution.findMin(nums=[3,4,5,1,2]))
