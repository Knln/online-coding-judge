from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        for i in range(1, len(nums)):
            temp = nums[i]

            j = i-1
            while j >= 0 and temp < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = temp

        return


solution = Solution()
solution.sortColors([2,0,2,1,1,0])
