from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        l = 0
        r = len(nums)-1

        while l <= r:

            mid = l + (r-l) // 2

            if target == nums[l]:
                return l

            if target == nums[r]:
                return r

            if nums[l] <= nums[mid]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[l]:
                    l = mid
                else:
                    r = mid

        return -1


solution = Solution()

print(solution.search(nums=[4,5,6,7,0,1,2], target=3))
print(solution.search(nums=[4,5,6,7,0,1,2], target=0))
print(solution.search(nums=[5,1,3], target=-0))